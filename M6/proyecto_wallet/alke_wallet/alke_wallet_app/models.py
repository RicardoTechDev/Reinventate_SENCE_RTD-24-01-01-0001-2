from django.db import models
from django.contrib.auth.models import User

class Compra(models.Model):
    #el id se crea de manera automática
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="compras")
    detalle     = models.CharField(max_length=255)
    total       = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True) 

    class Meta:
        #Permiso personalizado (opcional, aparecerá en el admin)
        permissions = [
            ("ver_lista_compras", "Puede ver el listado de compras realizadas")
        ]

    def __str__(self):
        return f"Compra #{self.id} - {self.user.username} - ${self.total}"


class Transferencia(models.Model):
    usuario_origen      = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transferencias")
    destinatario        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transferencias")
    created_at          = models.DateTimeField(auto_now_add=True) 


