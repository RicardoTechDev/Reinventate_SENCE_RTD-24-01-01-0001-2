from django.urls import path
from .views import authors_list

urlpatterns = [
    path("authors/", authors_list, name="authors_list"),
]