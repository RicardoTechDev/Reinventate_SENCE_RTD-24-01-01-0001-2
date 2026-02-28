from django.shortcuts import render
from datetime import date

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