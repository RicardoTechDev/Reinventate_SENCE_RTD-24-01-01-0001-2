from datetime import timezone

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError


class Wallet(models.Model):
    """
    Wallet o Billetera del usuario esto es 1 a 1
    - Un usuario tiene una sola wallet
    """
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        related_name="wallet", 
        on_delete=models.CASCADE
        )
    saldo       = models.IntegerField()
    activa      = models.BooleanField(default=True)
    moneda      = models.CharField(max_length=3, default='CLP')
    created_at  = models.DateTimeField(auto_now_add=True) #Se guarda al crear un registro
    updated_at  = models.DateTimeField(auto_now=True)#Se actualiza en cada save()

    def __str__(self):
        return f"Wallet({self.usuario})"


class CuentaBancaria(models.Model):
    """
    Cuentas bancarías propias asociadas al usuario (1 a N)
    recargar saldo, retiros, transferencias (según su lógica)
    """
    TIPO_CUENTA_CHOICES = [
    ("CTACTE", "Cuenta Corriente"),
    ("CTAAHORRO", "Cuenta Ahorro"),
    ("VISTA", "Cuenta Vista"),
    ("RUT", "Cuenta Rut"),
    ("OTRA", "Otro tipo de cuenta"),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,          # Si se elimina el usuario, se eliminan sus cuentas
        related_name="cuentas_bancarias"
    )

    alias               = models.CharField(max_length=60)
    banco               = models.CharField(max_length=80)
    tipo                = models.CharField(max_length=10, choices=TIPO_CUENTA_CHOICES, default="OTRA")
    numero              = models.CharField(max_length=40)  # string para permitir ceros/guiones
    rut_titular         = models.CharField(max_length=15, blank=True)
    email_notificacion  = models.EmailField(blank=True)
    es_principal        = models.BooleanField(default=False)
    verificada          = models.BooleanField(default=False)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)#Se actualiza en cada save()

    class Meta:
        # Evita duplicar la misma cuenta bancaria para el mismo usuario
        unique_together = ("usuario", "banco", "numero")

    def __str__(self):
        return f"{self.alias} - {self.banco} ({self.numero})"


class Tarjeta(models.Model):
    """
    Tarjetas propias del usuario (1 a N)
    """
    MARCA_CHOICES = [
        ("VISA", "Visa"),
        ("MC", "Mastercard"),
        ("AMEX", "American Express"),
        ("OTRA", "Otra"),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tarjetas"
    )

    alias           = models.CharField(max_length=60)
    marca           = models.CharField(max_length=10, choices=MARCA_CHOICES, default="OTRA")
    ultimos4        = models.CharField(max_length=4)
    exp_mes         = models.PositiveSmallIntegerField()
    exp_anio        = models.PositiveSmallIntegerField()

    # Token del gateway (Stripe/Transbank/etc.).
    # Lo dejamos null=True para evitar problemas de "unique_together" con string vacío.
    token           = models.CharField(max_length=255, null=True, blank=True)
    es_principal    = models.BooleanField(default=False)
    verificada      = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)#Se actualiza en cada save()

    class Meta:
        # Evita duplicar el mismo token para el mismo usuario
        unique_together = ("usuario", "token")

    def __str__(self):
        return f"{self.alias} ({self.marca} ****{self.ultimos4})"


class Beneficiario(models.Model):
    """
    Beneficiarios (cuentas de terceros) para transferencias (1 a N).
    """
    TIPO_CUENTA     = CuentaBancaria.TIPO_CUENTA_CHOICES
    usuario         = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="beneficiarios")
    alias           = models.CharField(max_length=60)
    nombre          = models.CharField(max_length=120, blank=True)
    rut             = models.CharField(max_length=15, blank=True)
    email           = models.EmailField(blank=True)
    banco           = models.CharField(max_length=80)
    tipo            = models.CharField(max_length=10, choices=TIPO_CUENTA, default="OTRA")
    numero          = models.CharField(max_length=40)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)#Se actualiza en cada save()

    class Meta:
        # Evita duplicar el mismo beneficiario bancario para el mismo usuario
        unique_together = ("usuario", "banco", "numero")

    def __str__(self):
        return f"{self.alias} - {self.banco} ({self.numero})"


class Transferencia(models.Model):
    """
    Transferencias desde una wallet a un beneficiario.

    Nota:
    - El usuario que transfiere se obtiene con: transferencia.wallet.usuario
    (no se duplica campo usuario aquí para evitar inconsistencias).
    """
    ESTADO_CHOICES = [
        ("PEND", "Pendiente"),
        ("OK", "Exitosa"),
        ("RECH", "Rechazada"),
    ]

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.PROTECT,          # Protege historial (no borrar wallet si hay transferencias)
        related_name="transferencias"
    )
    beneficiario = models.ForeignKey(
        Beneficiario,
        on_delete=models.PROTECT,          # Protege historial (no borrar beneficiario si hay transferencias)
        related_name="transferencias"
    )

    monto = models.DecimalField(max_digits=14, decimal_places=2)
    concepto = models.CharField(max_length=120, blank=True)

    estado = models.CharField(max_length=4, choices=ESTADO_CHOICES, default="PEND")

    created_at = models.DateTimeField(default=timezone.now)  # registro de la transferencia
    procesada_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.wallet.usuario} -> {self.beneficiario.alias} (${self.monto})"


class Compra(models.Model):
    #el id se crea de manera automática
    """
    Compras pagadas con saldo wallet o (opcional) con tarjeta asociada.
    """
    ESTADO_CHOICES = [
        ("PEND", "Pendiente"),
        ("OK", "Exitosa"),
        ("RECH", "Rechazada"),
    ]
    METODO_CHOICES = [
        ("WALLET", "Saldo Wallet"),
        ("TARJETA", "Tarjeta"),
    ]

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.PROTECT,
        related_name="compras"
    )

    comercio = models.CharField(max_length=120)
    monto = models.DecimalField(max_digits=14, decimal_places=2)
    metodo_pago = models.CharField(max_length=10, choices=METODO_CHOICES, default="WALLET")
    # Si metodo_pago = TARJETA, aquí guardas cuál se usó (opcional)
    tarjeta = models.ForeignKey(
        Tarjeta,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="compras"
    )

    estado = models.CharField(max_length=4, choices=ESTADO_CHOICES, default="PEND")
    referencia = models.CharField(max_length=120, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        #Permiso personalizado (opcional, aparecerá en el admin)
        permissions = [
            ("ver_lista_compras", "Puede ver el listado de compras realizadas"),
            ("modificar_compra", "Modificar una compra"),
            
        ]

    def __str__(self):
        return f"Compra #{self.id} - {self.user.username} - ${self.total}"


class Recarga(models.Model):
    """
    Recargas (entradas de dinero) a la wallet desde:
    - Cuenta bancaria propia
    - Tarjeta asociada
    """
    ESTADO_CHOICES = [
        ("PEND", "Pendiente"),
        ("OK", "Exitosa"),
        ("RECH", "Rechazada"),
    ]
    ORIGEN_CHOICES = [
        ("BANCO", "Cuenta Bancaria"),
        ("TARJETA", "Tarjeta"),
    ]

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.PROTECT,
        related_name="recargas"
    )

    monto = models.DecimalField(max_digits=14, decimal_places=2)

    origen = models.CharField(max_length=10, choices=ORIGEN_CHOICES)

    cuenta_bancaria = models.ForeignKey(
        CuentaBancaria,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="recargas"
    )
    tarjeta = models.ForeignKey(
        Tarjeta,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="recargas"
    )

    estado = models.CharField(max_length=4, choices=ESTADO_CHOICES, default="PEND")

    created_at = models.DateTimeField(default=timezone.now)

    def clean(self):
        """
        Validación lógica:
        - Si origen = BANCO => cuenta_bancaria obligatoria y tarjeta debe ser None
        - Si origen = TARJETA => tarjeta obligatoria y cuenta_bancaria debe ser None
        """
        super().clean()

        if self.origen == "BANCO":
            if not self.cuenta_bancaria:
                raise ValidationError({"cuenta_bancaria": "Debes seleccionar una cuenta bancaria."})
            if self.tarjeta:
                raise ValidationError({"tarjeta": "No debe venir tarjeta cuando el origen es BANCO."})

        if self.origen == "TARJETA":
            if not self.tarjeta:
                raise ValidationError({"tarjeta": "Debes seleccionar una tarjeta."})
            if self.cuenta_bancaria:
                raise ValidationError({"cuenta_bancaria": "No debe venir cuenta bancaria cuando el origen es TARJETA."})

    def __str__(self):
        return f"Recarga (${self.monto})"


class Movimiento(models.Model):
    """
    Movimientos de la wallet (historial/auditoría del saldo).
    - Registra entradas (crédito) y salidas (débito).
    - Permite reconstruir y auditar el saldo.
    """
    TIPO_CHOICES = [
        ("RECARGA", "Recarga"),
        ("TRANSFER", "Transferencia"),
        ("COMPRA", "Compra"),
        ("AJUSTE", "Ajuste"),
    ]
    DIRECCION_CHOICES = [
        ("CRED", "Crédito (+)"),
        ("DEB", "Débito (-)"),
    ]

    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.PROTECT,
        related_name="movimientos"
    )

    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    direccion = models.CharField(max_length=4, choices=DIRECCION_CHOICES)

    monto = models.DecimalField(max_digits=14, decimal_places=2)

    # Guardar el saldo resultante es opcional, pero muy útil para reportes rápidos
    saldo_despues = models.DecimalField(max_digits=14, decimal_places=2, null=True, blank=True)

    # Enlaces opcionales al evento que generó el movimiento
    transferencia = models.OneToOneField(
        Transferencia,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="movimiento"
    )
    compra = models.OneToOneField(
        Compra,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="movimiento"
    )
    recarga = models.OneToOneField(
        Recarga,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="movimiento"
    )

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.get_tipo_display()} {self.get_direccion_display()} ${self.monto}"


