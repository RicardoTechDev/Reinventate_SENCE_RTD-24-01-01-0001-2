from django.shortcuts import render
from .models import Author, Book, Publisher

def authors_list(request):
    autores = Author.objects.all()#SELECT * FROM Authors

    contexto = {
        "autores" : autores,
    } 

    return render(request, "authors_list.html", contexto)


def publishers_list(request):
    publishers = Publisher.objects.all()#SELECT * FROM Authors
    publishers = list(publishers)
    contexto = {
        "publishers" : publishers,
    } 

    return render(request, "publishers_list.html", contexto)
