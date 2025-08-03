from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('book_list/', views.book_list, name='book_list'),
    path('books/', views.view_books, name='view_books'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
]

