from .models import Book
from django.forms import ModelForm, TextInput


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "cupboard_number", "shelf_number", "comment"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите автора'
            }),
            "cupboard_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер шкафа'
            }),
            "shelf_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер полки'
            }),
            "comment": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Добавьте комментарий'
            })
        }
