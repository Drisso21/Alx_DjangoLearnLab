from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Logic to create a book
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    # Logic to edit a book
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    # Logic to delete a book
    pass
