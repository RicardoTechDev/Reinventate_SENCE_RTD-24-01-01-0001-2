from django.shortcuts import render
from .models import Author, Book, Publisher

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
    publishers = Publisher.objects.values("id", "name")#SELECT * FROM Authors
    publishers = list(publishers)
    contexto = {
        "publishers" : publishers,
    } 

    return render(request, "publishers_list.html", contexto)
