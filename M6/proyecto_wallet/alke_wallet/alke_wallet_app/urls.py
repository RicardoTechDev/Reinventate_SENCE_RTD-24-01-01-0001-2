from django.urls import path

from .views import (login_view, home_view, compras_view, 
                    contacto_view, contacto_manual_view)

urlpatterns = [
    path("", login_view, name="login"),
    path("home/", home_view, name="home"),
    path("compras/", compras_view, name="compras"),
    path("contacto/", contacto_view, name="contacto"),
    path("contacto-manual/", contacto_manual_view, name="contacto_manual"),
]