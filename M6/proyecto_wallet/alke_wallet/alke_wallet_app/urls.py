from django.urls import path

from .views import login_view, home_view, compras_view

urlpatterns = [
    path("", login_view, name="login"),
    path("home/", home_view, name="home"),
    path("compras/", compras_view, name="compras"),
]