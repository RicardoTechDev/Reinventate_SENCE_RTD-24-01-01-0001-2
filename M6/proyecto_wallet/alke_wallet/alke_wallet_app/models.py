from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


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

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        related_name="cuenta_bancaria", 
        on_delete=models.CASCADE
        )
    numero =
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CUENTA_CHOICES,
        default="OTRA",
    )
    banco =
    rut_titular =
    correo_notificacion=
    activa =
    created_at  = "DD-MM-YYYY"
    updated_at  = "DD-MM-YYYY"


class Tarjeta(models.Model):
    """
    Tarjetas propias del usuario (1 a N)
    """
    pass


class Beneficiario(models.Model):
    pass


class Transferencia(models.Model):
    pass

class Movimiento(models.Model):
    pass


class Recarga(models.Model):
    pass


class Compra(models.Model):
    #el id se crea de manera automática
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="compras")
    detalle     = models.CharField(max_length=255, blak=True)
    total       = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True) 

    class Meta:
        #Permiso personalizado (opcional, aparecerá en el admin)
        permissions = [
            ("ver_lista_compras", "Puede ver el listado de compras realizadas"),
            ("modificar_compra", "Modificar una compra"),
            
        ]

    def __str__(self):
        return f"Compra #{self.id} - {self.user.username} - ${self.total}"





