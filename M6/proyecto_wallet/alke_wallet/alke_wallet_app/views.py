from django.shortcuts import render

# Create your views here.
def login_view(request):
    contex = {
        "usuario" : "nombre_usuario"
    }
    return render(request, "login/login.html", contex)
