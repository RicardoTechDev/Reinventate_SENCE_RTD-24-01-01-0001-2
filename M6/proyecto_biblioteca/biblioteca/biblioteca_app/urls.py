from django.urls import path
from .views import (authors_list, publishers_list, book_list, 
                    authors_create, authors_update, authors_delete,
                    books_create, books_update, books_delete,
                    publisher_create, publisher_update, publisher_delete)

urlpatterns = [
    #Autores
    path("authors/", authors_list, name="authors_list"),
    path("authors/new", authors_create, name="authors_create"),
    path("authors/<int:pk>/edit/", authors_update, name="authors_update"),
    path("authors/<int:pk>/delete/", authors_delete, name="authors_delete"),

    #Publicaciones
    path("publishers/", publishers_list, name="publishers_list"),
    path("publishers/new", publisher_create, name="publisher_create"),
    path("publishers/<int:pk>/edit/", publisher_update, name="publisher_update"),
    path("publishers/<int:pk>/delete/", publisher_delete, name="publisher_delete"),

    #Libros
    path("books/", book_list, name="book_list"),
    path("books/new", books_create, name="books_create"),
    path("books/<int:pk>/edit/", books_update, name="books_update"),
    path("books/<int:pk>/delete/", books_delete, name="books_delete"),
]