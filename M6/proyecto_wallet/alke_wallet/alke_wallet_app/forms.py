#Importación del módulo de formularios de Django
from django import forms

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
        label = "Nombre", #texto que se usará al mostrar el nombre dedl campo en el template
        max_length = 150, #Validación, no permite más de 150 caracteres
        )
    
    email = forms.EmailField(
        label = "Email",
    )

    mensaje = forms.CharField(
        label = "Mensaje"
    )