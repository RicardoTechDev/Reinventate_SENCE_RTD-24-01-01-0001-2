from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import date
from .forms import ContactoForm
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required


# Create your views here.
def login_view(request):
    #Si ya está logueado lo redirijimos al home (opcional)
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == 'POST':
        username = (request.POST.get("email") or "").strip()
        password = (request.POST.get("password") or "").strip()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)#Crear la sesión (queda logueado)
            return redirect("home")
        
        else:
            #Credenciales invalidas
            messages.error(request,"Debe ingresar un RUT.Usuario o contraseña incorrectos.")
    
    return render(request, "login/login.html")


def logut_view(request):
    logout(request)#cerrar la sesion
    return redirect('login')
    

def signup_view(request):
        #Si ya está logueado lo redirijimos al home (opcional)
    if request.user.is_autenticated:
        return redirect("home")
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()# Aquí estamos creando el usuario, insertando en la BD

            messages.success(request, "Cuenta creada correctamente. ¡Bienvenido!")

            return redirect('login')

    else:
        form = UserCreationForm()
        contex = {
            "form":form
            }
    return render(request, "register/register.html", contex)

@login_required
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

@login_required
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
            return render(request, "contacto_ok/page.html", contex)
        
        #7) Si no es válido form.is_valid(), no entramos al return
        #y caemos en el render final de la función con:
        # - form con errores (form.errors)
        # - el template puede mostrar esos errores
        else:
            print(form.errors)

    else:
        form = ContactoForm()#se crea una instancia vacía

    return render(request, "contacto/page.html", {"form": form})


def contacto_manual_view(request):
    errores = {}
    valores = {"nombre": "", "email": "", "mensaje": ""}

    if request.method == "POST":
        nombre = (request.POST.get("nombre") or "").strip()
        email = (request.POST.get("email") or "").strip()
        mensaje = (request.POST.get("mensaje") or "").strip()

        valores = {"nombre": nombre, "email": email, "mensaje": mensaje}

        if not nombre:
            errores["nombre_error"] = "El nombre es obligatorio"
        elif len(nombre) > 150:
            errores["nombre_error"] = "El nombre no puede superar los 150 caracteres"

        if not email:
            errores["email_error"] = "El email es obligatorio"
        else:
            try:
                validate_email(email)
            except ValidationError:
                errores["email_error"] = "El email es inválido"

        if not mensaje:
            errores["mensaje_error"] = "El mensaje es obligatorio"

        if not errores:
            contex = {
                    "nombre" : nombre,
                    "email" :  email,
                    "mensaje": mensaje
                }
            return render(request, "contacto_ok/page.html", contex)

    context = {
        "errores" : errores,
        "valores" : valores
    }
    return render(request, "contacto_manual/page.html", context)
