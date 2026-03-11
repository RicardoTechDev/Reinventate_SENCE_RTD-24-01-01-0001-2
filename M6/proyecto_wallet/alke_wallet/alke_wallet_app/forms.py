#Importación del módulo de formularios de Django
from django import forms
from .models import CuentaBancaria

#Creación de una nueva clase  que hereda de forms.Form
#"forms"  trae las clases para dedfinir formularios y campos con validación
class ContactoForm(forms.Form):
    '''
    Definimos un formulario clásico, aquí describes:
    * Qué campos tendrá el formulario
    * Qué tipo de datos espera cada campo
    * Qué validaciones se debe aplicar (largo, requerido, formato, etc)
    '''

    nombre = forms.CharField(
        label = "Nombre", #texto que se usará al mostrar el nombre del campo en el template
        max_length = 150, #Validación, no permite más de 150 caracteres
        error_messages={
            "required": "El campo nombre es obligatorio.",
            "max_length": "El nombre no puede superar los 150 caracteres"
        },
        widget=forms.TextInput(attrs={"class": "form-control"})
        )
    
    email = forms.EmailField(
        label = "Email",
        error_messages={
            "required": "El campo email es obligatorio.",
            "invalid": "Ingresa un correo válido"
        },
        widget=forms.EmailInput (attrs={"class": "form-control"})
    )

    mensaje = forms.CharField(
        label = "Mensaje",
        error_messages={
            "required": "El campo mensaje es obligatorio."
        },
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Escribe aquí tu mensaje..."})
    )



class CuentaBancariaForm(forms.ModelForm):
    class Meta:
        model = CuentaBancaria
        fields = [
            "alias", "banco", "tipo", "numero",
            "rut_titular", "email_notificacion",
            "es_principal", "verificada",
        ]