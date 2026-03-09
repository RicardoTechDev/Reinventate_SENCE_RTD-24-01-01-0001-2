from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    """
    Wallet o Billetera del usuario esto es 1 a 1
    - Un usuario tiene una sola wallet
    """
    pass


class CuentaBancaria(models.Model):
    """
    Cuentas bancarías propias asociadas al usuario (1 a N)
    recargar saldo, retiros, transferencias (según su lógica)
    """
    pass


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





