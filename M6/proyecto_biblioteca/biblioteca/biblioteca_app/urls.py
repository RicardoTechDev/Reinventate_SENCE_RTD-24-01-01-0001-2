from django.urls import path
from .views import authors_list, publishers_list

urlpatterns = [
    #Autores
    path("authors/", authors_list, name="authors_list"),
    
    #Publicaciones
    path("publishres/", publishers_list, name="publishers_list"),

    #Libros
]