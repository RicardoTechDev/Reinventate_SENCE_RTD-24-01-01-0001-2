from django.shortcuts import get_object_or_404, render, redirect
from .models import Author, Book, Publisher
from django.db.models import Count
from .forms import AuthorForm, BookForm
from django.http import Http404
from django.contrib import messages

#DOCUMENTACIÓN: https://docs.djangoproject.com/en/6.0/topics/http/decorators/
from django.views.decorators.http import require_POST

# Alternativa a require_POST: 
from django.views.decorators.http import require_http_methods
# Ejemplo decorador: @require_http_methods(["GET", "POST"])


#----------------------
# Author
#----------------------
@require_http_methods(["GET"])
def authors_list(request):
    autores = Author.objects.all().order_by("name")#SELECT * FROM Authors

    contexto = {
        "autores" : autores,
    } 

    return render(request, "authors_list.html", contexto)


@require_http_methods(["GET", "POST"])
def authors_create(request):
    if request.method == "POST":#Si es POST
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Autor creado de manera correcta")
            return redirect("authors_list")

        else:
            messages.error(request, "No fue posible crear el autor")
        
    else:
        form = AuthorForm()#se crea una instancia vacía

    return render(request, "authors_form.html", {"form": form, "modo": "crear"})


@require_http_methods(["GET", "POST"])
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
            messages.success(request, "Autor actualizado de manera correcta")
            return redirect("authors_list")
        
        else:
            messages.error(request, "No fue posible actualizar el autor")
        
    else:
        form = AuthorForm(instance = autor)

    return render(request, "authors_form.html", {"form": form, "modo": "editar"})


@require_POST
def authors_delete(request, pk):
    try:
        autor = get_object_or_404(Author, id=pk)
        autor.delete()
        messages.success(request, "Autor eliminado correctamente")
    except Exception:
        messages.error(request, "Ocurrió un error al intentar eliminar el autor")
    
    return redirect("authors_list")

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
    form = BookForm()

    contexto = {
        "libros" : libros,
        "form"   : form,
        'modo': 'crear',
    } 

    return render(request, "books_list.html", contexto)


@require_http_methods(["POST"])
def books_create(request):
    if request.method == "POST":#Si es POST
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Libro creado de manera correcta")
            return redirect("book_list")

        messages.error(request, "No fue posible crear el libro")        
        libros = Book.objects.select_related("author").order_by("title")
        context = {
            'libros' : libros,
            'modo': 'crear',
            'form': form,
        }
        return render(request, "books_list.html", context)
    
@require_http_methods(["GET", "POST"])
def books_update(request, pk):
    libro = get_object_or_404(Book, id=pk)
    libros = Book.objects.select_related("author").order_by("title")

    if request.method == 'POST':
        form = BookForm(request.POST, instance=libro)

        if form.is_valid():
            form.save()
            messages.success(request, "Libro actualizado de manera correcta")
            return redirect("book_list")
        
        messages.error(request, "No fue posible actuializar el libro")        
        
        context = {
            'libros' : libros,
            'modo': 'editar',
            'form': form,
            'abrir_modal': True
        }
        return render(request, "books_list.html", context)
    
    form = BookForm(instance=libro)
    context = {
            'libros' : libros,
            'modo': 'editar',
            'form': form,
            'abrir_modal': True
        }
    return render(request, "books_list.html", context)


@require_POST
def books_delete(request, pk):
    try:
        libro = get_object_or_404(Book, id=pk)
        libro.delete()
        messages.success(request, "Libro eliminado correctamente")
    except Exception:
        messages.error(request, "Ocurrió un error al intentar eliminar el libro")
    
    return redirect("book_list")