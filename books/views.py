from django.http.response import Http404
from django.shortcuts import render

from .models import *
# Create your views here.


def index(request):
    return render(request, 'books/index.html', None)


def book(request, book_id: int):
    try:
        b = Book.objects.get(pk=book_id)
    except Http404:
        raise Http404(f'No book with id ${book_id} found')

    return render(request, 'books/book.html', {'book': b})


def books_list(request):
    book_list = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': sorted(book_list)})
