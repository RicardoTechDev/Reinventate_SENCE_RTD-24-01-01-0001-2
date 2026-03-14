from django.shortcuts import get_object_or_404, render, redirect
from .models import Author, Book, Publisher
from django.db.models import Count
from .forms import AuthorForm
from django.http import Http404

#----------------------
# Author
#----------------------
def authors_list(request):
    autores = Author.objects.all().order_by("name")#SELECT * FROM Authors

    contexto = {
        "autores" : autores,
    } 

    return render(request, "authors_list.html", contexto)


def authors_create(request):
    if request.method == "POST":#Si es POST
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("authors_list")
        
    else:
        form = AuthorForm()#se crea una instancia vacía

    return render(request, "authors_form.html", {"form": form, "modo": "crear"})


def authors_update(request, pk):
    autor = get_object_or_404(Author, id=pk)

    #! Versión manual o más extensa que get_object_or_404
    # try:
    #     autor = Author.objects.get(id=pk)
    # except Author.DoesNotExist:
    #     raise Http404("Autor no encontrado")

    if request.method == "POST":#Si es POST
        form = AuthorForm(request.POST, instance = autor)

        if form.is_valid():
            form.save()
            return redirect("authors_list")
        
    else:
        form = AuthorForm(instance = autor)

    return render(request, "authors_form.html", {"form": form, "modo": "editar"})


def authors_delete(request, pk):
    autor = get_object_or_404(Author, id=pk)
    autor.delete()



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


#----------------------
# Book
#----------------------
def book_list(request):
    '''
    Recuperar información de la base de datos
    Ejemplos:

    1.- libros = Book.objects.all()
    2.- libros = Book.objects.value('id', 'name')
    3.- libros = Book.objects.get(name="nombre_libro") --> puede ser cualquier campo como id u otro
    4.- libros = Book.objects.filter(title__icontains="Harry") --> Libros que el título contenga "Harry"
    5.- libros = Book.objects.filter(title__startswith="hola") --> libros que el título comience con "hola"
    6.- Limitación QuerySet:  
                            - Book.objects.all()[:5]  --> esto devuelve los primeros 5 objetos
                            - Book.objects.all()[5:10] --> esto devuelve los objetos del sexto al décimo

    Ejemplo para insertar un registro

    1° Paso recuperar el autor (una instancia) --> this_author = Author.objects.get(id=2)
    2° Paso creamos un nuevo registro my_book = Book.objects.create(title="Little Women", author=this_author)	# establecer el autor recuperado como el autor de un nuevo libro

    # o en una línea...
    my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2)

    Ejemplo de actualización
    
    libro_recuperado = Book.objects.get(id=1)
    libro_recuperado.title = "Nuevo título"
    libro_recuperado.save()

    Ejmplo de eliminación
    1° Foma larga
    libro_recuperado = Book.objects.get(id=1)
    libro_recuperado.delete()

    2° Forma corta
    Book.objects.get(id=1).delete()

    '''

    '''
    select_related
    (https://docs.djangoproject.com/en/6.0/ref/models/querysets/#django.db.models.query.QuerySet.select_related)

    Devuelve un QuerySet que "seguirá" las relaciones de clave externa (clave foranea), 
    seleccionando datos adicionales de objetos relacionados al ejecutar su consulta. 
    Esto mejora el rendimiento, ya que genera una consulta más compleja, 
    pero evita que el uso posterior de relaciones de clave externa requiera 
    consultas a la base de datos.
    '''

    libros = Book.objects.select_related("author").order_by("title")

    contexto = {
        "libros" : libros,
    } 

    return render(request, "books_list.html", contexto)