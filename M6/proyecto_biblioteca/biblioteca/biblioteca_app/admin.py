from django.contrib import admin
from .models import Author, Book, Publisher

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    list_filter = ("created_at",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created_at", "updated_at")
    list_filter = ("created_at",)
    search_fields = ("title",)
    ordering = ("title",)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    list_filter = ("created_at",)
    search_fields = ("name",)
    ordering = ("name",)