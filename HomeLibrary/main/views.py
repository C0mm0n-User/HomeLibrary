from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def index(request):
    books = Book.objects.order_by('author', 'title')
    return render(request, 'main/index.html', {'books': books})


def add(request):
    error = ''
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма заполнена некорректно! Перезаполните все поля и повторите попытку.'

    form = BookForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add.html', context)
