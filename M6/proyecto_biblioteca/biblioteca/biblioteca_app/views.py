from django.shortcuts import render
from .models import Author, Book, Publisher
from django.db.models import Count

#----------------------
# Author
#----------------------
def authors_list(request):
    autores = Author.objects.all()#SELECT * FROM Authors

    contexto = {
        "autores" : autores,
    } 

    return render(request, "authors_list.html", contexto)


#----------------------
# Publisher
#----------------------
def publishers_list(request):
    publishers = Publisher.objects.annotate(total_libros=Count("books")).values("id", "name", "total_libros")#SELECT * FROM Authors
    publishers = list(publishers)
    contexto = {
        "publishers" : publishers,
    } 

    return render(request, "publishers_list.html", contexto)
