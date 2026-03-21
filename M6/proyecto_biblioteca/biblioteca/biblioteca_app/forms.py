from django import forms
from .models import Author, Book, Publisher


class AuthorForm(forms.ModelForm):
    name = forms.CharField(
        label = "Nombre", #texto que se usará al mostrar el nombre del campo en el template
        max_length = 255, #Validación, no permite más de 150 caracteres
        error_messages={
            "required": "El campo nombre es obligatorio.",
            "max_length": "El nombre no puede superar los 255 caracteres"
        },
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del autor"})
        )

    class Meta:
        model = Author
        fields = ["name"]


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]
        widgets= {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Ingrese el título del libro'
            }),
            'author': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ["name", "books"]
        widgets= {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Ingrese el nombre de la publicación'
            }),
            'books': forms.SelectMultiple(attrs={
                'class': 'form-select',
            }),
        }