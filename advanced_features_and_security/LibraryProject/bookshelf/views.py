from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('publication_year')

        # Création du livre
        Book.objects.create(title=title, author=author, publication_year=year)
        return redirect('/')  # redirection vers la liste

    return render(request, 'bookshelf/add_book.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Create your views here.
