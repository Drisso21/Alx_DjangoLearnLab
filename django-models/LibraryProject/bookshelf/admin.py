from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # colonnes affichées
    list_filter = ('publication_year', 'author')  # filtres dans la sidebar
    search_fields = ('title', 'author')  # champ de recherche en haut

admin.site.register(Book, BookAdmin)