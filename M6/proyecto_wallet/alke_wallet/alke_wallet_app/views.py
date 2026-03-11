from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import date
from .forms import ContactoForm, CuentaBancariaForm
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from .models import Wallet, CuentaBancaria


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
            messages.error(request,"Usuario o contraseña incorrectos.")
    
    return render(request, "login/login.html", )


def logut_view(request):
    logout(request)#cerrar la sesion
    return redirect('login')
    

def signup_view(request):
        #Si ya está logueado lo redirijimos al home (opcional)
    if request.user.is_authenticated:
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
    # 1) Asegurar que el usuario tenga wallet (si no existe, se crea)
    wallet, creada = Wallet.objects.get_or_create(
        usuario=request.user,
        defaults={"saldo": 0, "activa": True, "moneda": "CLP"}
    )

    # (opcional) si quieres mostrar mensaje solo cuando se crea
    # if creada:
    #     messages.success(request, "Wallet creada automáticamente")

    context = {
        "titulo_principal": "Home Alke Wallet",
        "titulo_card": "Bienvenido a mi proyecto web con Django",
        "hoy": date.today(),
        "wallet": wallet,
        "noticias": ["Django es rápido", "Django es extremadamente facil", "Templates son útiles"],
    }

    return render(request, "home/page.html", context)


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



@login_required
def cuentas_bancarias_list_view(request):
    """
    Lista las cuentas bancarias asociadas al usuario.
    """
    cuentas = CuentaBancaria.objects.filter(usuario=request.user).order_by("-created_at")
    return render(request, "wallet/cuentas_list.html", {"cuentas": cuentas})


@login_required
def cuenta_bancaria_create_view(request):
    """
    Crea una cuenta bancaria asociada al usuario logueado.
    """
    if request.method == "POST":
        form = CuentaBancariaForm(request.POST)
        if form.is_valid():
            cuenta = form.save(commit=False)
            cuenta.usuario = request.user  # Asegura dueño
            cuenta.save()

            # (opcional) si se marca como principal, desmarcar otras
            if cuenta.es_principal:
                CuentaBancaria.objects.filter(usuario=request.user).exclude(id=cuenta.id).update(es_principal=False)

            messages.success(request, "Cuenta bancaria creada")
            return redirect("wallet:cuentas_list")
    else:
        form = CuentaBancariaForm()

    return render(request, "wallet/cuenta_form.html", {"form": form, "modo": "crear"})


@login_required
def cuenta_bancaria_update_view(request, cuenta_id):
    """
    Edita una cuenta bancaria del usuario.
    get_object_or_404 + filtro por usuario => evita editar cuentas ajenas.
    """
    cuenta = get_object_or_404(CuentaBancaria, id=cuenta_id, usuario=request.user)

    if request.method == "POST":
        form = CuentaBancariaForm(request.POST, instance=cuenta)
        if form.is_valid():
            cuenta = form.save()

            if cuenta.es_principal:
                CuentaBancaria.objects.filter(usuario=request.user).exclude(id=cuenta.id).update(es_principal=False)

            messages.success(request, "Cuenta bancaria actualizada")
            return redirect("wallet:cuentas_list")
    else:
        form = CuentaBancariaForm(instance=cuenta)

    return render(request, "wallet/cuenta_form.html", {"form": form, "modo": "editar", "cuenta": cuenta})


@login_required
def cuenta_bancaria_delete_view(request, cuenta_id):
    """
    Elimina una cuenta bancaria del usuario.
    """
    cuenta = get_object_or_404(CuentaBancaria, id=cuenta_id, usuario=request.user)

    if request.method == "POST":
        cuenta.delete()
        messages.success(request, "Cuenta bancaria eliminada")
        return redirect("wallet:cuentas_list")

    return render(request, "wallet/cuenta_confirm_delete.html", {"cuenta": cuenta})