from django.urls import path

from .views import (login_view, home_view, compras_view, 
                    contacto_view, contacto_manual_view,
                    logut_view, signup_view, wallet_detalle_view,
                    cuentas_bancarias_list_view,
                    cuenta_bancaria_create_view,
                    cuenta_bancaria_update_view,
                    cuenta_bancaria_delete_view,)

urlpatterns = [
    path("", login_view, name="login"),
    path("logout/", logut_view, name="logout"),
    path("signup/", signup_view, name="signup"),
    path("home/", home_view, name="home"),
    path("compras/", compras_view, name="compras"),
    path("contacto/", contacto_view, name="contacto"),
    path("contacto-manual/", contacto_manual_view, name="contacto_manual"),
    path("wallet/", wallet_detalle_view, name="wallet_detalle"),
    path("wallet/cuentas/", cuentas_bancarias_list_view, name="cuentas_list"),
    path("wallet/cuentas/nueva/", cuenta_bancaria_create_view, name="cuenta_create"),
    path("wallet/cuentas/<int:cuenta_id>/editar/", cuenta_bancaria_update_view, name="cuenta_update"),
    path("wallet/cuentas/<int:cuenta_id>/eliminar/", cuenta_bancaria_delete_view, name="cuenta_delete"),
]