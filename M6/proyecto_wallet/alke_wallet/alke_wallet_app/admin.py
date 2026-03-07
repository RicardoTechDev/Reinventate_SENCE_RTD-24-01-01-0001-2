from django.contrib import admin
from .models import Compra

#1° Forma, simple
#admin.site.register(Compra)

#2° Forma más pro
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "detalle", "total", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username", "user__email")
    ordering = ("created_at",)