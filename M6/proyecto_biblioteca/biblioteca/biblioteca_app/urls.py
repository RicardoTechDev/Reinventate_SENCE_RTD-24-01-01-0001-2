from django.urls import path
from .views import (authors_list, publishers_list, book_list, 
                    authors_create, authors_update, authors_delete)

urlpatterns = [
    #Autores
    path("authors/", authors_list, name="authors_list"),
    path("authors/new", authors_create, name="authors_create"),
    path("authors/<int:pk>/edit/", authors_update, name="authors_update"),
    path("authors/<int:pk>/delete/", authors_delete, name="authors_delete"),

    #Publicaciones
    path("publishres/", publishers_list, name="publishers_list"),

    #Libros
    path("books/", book_list, name="book_list"),
]