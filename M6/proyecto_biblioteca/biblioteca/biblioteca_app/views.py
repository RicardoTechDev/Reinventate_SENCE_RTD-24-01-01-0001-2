from django.shortcuts import render
from .models import Author

def authors_list(request):
    autores = Author.objects.all()#SELECT * FROM Authors

    contexto = {
        "autores" : autores,
    } 

    return render(request, "authors_list.html", contexto)
