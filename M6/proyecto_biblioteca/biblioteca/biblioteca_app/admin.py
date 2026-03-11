from django.contrib import admin
from .models import Author

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    list_filter = ("created_at",)
    search_fields = ("name",)
    ordering = ("name",)