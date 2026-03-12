from django.urls import path
from .views import authors_list, publishers_list, book_list

urlpatterns = [
    #Autores
    path("authors/", authors_list, name="authors_list"),
    
    #Publicaciones
    path("publishres/", publishers_list, name="publishers_list"),

    #Libros
    path("books/", book_list, name="book_list"),
]