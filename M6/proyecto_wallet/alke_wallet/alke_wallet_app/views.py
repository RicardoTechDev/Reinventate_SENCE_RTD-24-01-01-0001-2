from django.shortcuts import render
from datetime import date
from .forms import ContactoForm

# Create your views here.
def login_view(request):
    return render(request, "login/login.html")


def home_view(request):
    contex = {
        "titulo_principal" : "Home Alke Wallet",
        "titulo_card": "Bienvenido a mi proyecto web con Django",
        "usuario": {
            'first_name': 'Luis', 
            'last_name': 'Salazar'
            },
        "hoy": date.today(),
        "noticias": ["Django es rápido", "Django es extremadamente facil", "Templates son útiles"],
    }
    return render(request, "home/page.html", contex)


def compras_view(request):
    contex = {
        "titulo_pagina" : "Home Alke Wallet",
        "hoy": date.today(),
        "total_compras": "768.475"
    }
    return render(request, "compras/page.html", contex)

def contacto_view(request):
    '''
    "request" es el objeto que reprenta la petición que se realiza 
    desde el cliente (navegador)

    Trea información como:
    * request.method (GET / POST)
    * request.POST (datos enviados desde el formulario)
    * request.user
    '''
    #1) Si  el usuario envía el formulario (botón enviar/submit)
    #normalmente el navegador lo envía con método POST
    if request.method == "POST":#Si es POST
        
        #2) Creamos una instancia del formulario se rellena con los datos enviados
        # request.POST e sun diccionario con lo que llegó desde el <form>
        # ejemplo {"nombre": "", "email": "", "mensaje": ""}
        form = ContactoForm(request.POST)

        #3) is_valid() ejecuta todas las validaciones del form
        # ejemplo: 
        # - Campos requeridos 
        # - Email invalido
        # - max_length, entre otros
        #Si algo falla, form.errors se llena con los mensajes de error y 
        #form.is_valid() sería igual a False 
        
        if form.is_valid():
            #4) cleaned_data trae los datos ya validados y "limpios":
            # - strings con strip, conversiones de tipos de datos, etc.
            # - solo existe si is_valid() fue True

            nombre = form.cleaned_data["nombre"]
            email = form.cleaned_data["email"]
            mensaje = form.cleaned_data["mensaje"]

            #5)Aquí realizariamos el procesamiento de la data o info:
            # -guardar en BD
            # -Enviar un correo
            # -crear un ticket, etc.

            #6) Indicar al usuario que todo se proceso de manera correcta
            contex = {
                "nombre" : nombre,
                "email" :  email,
                "mensaje": mensaje
            }
            return render(request, "name.html", contex)
        
        #7) Si no es válido form.is_valid(), no entramos al return
        #y caemos en el render final de la función con:
        # - form con errores (form.errors)
        # - el template puede mostrar esos errores
        else:
            print(form.errors)

    else:
        form = ContactoForm()

    return render(request, "contacto/page.html", {"form": form})