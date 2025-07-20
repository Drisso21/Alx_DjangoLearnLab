import os
import django
from relationship_app.models import Author, Book, Library, Librarian


#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
#django.setup()


# Authors
a1 = Author.objects.create(name="George Orwell")
a2 = Author.objects.create(name="Jane Austen")

# Books
b1 = Book.objects.create(title="1984", author=a1)
b2 = Book.objects.create(title="Animal Farm", author=a1)
b3 = Book.objects.create(title="Pride and Prejudice", author=a2)

# Libraries
lib1 = Library.objects.create(name="Central Library")
lib2 = Library.objects.create(name="City Library")

# Assign books to libraries
lib1.books.set([b1, b2])   # Central Library has Orwell's books
lib2.books.set([b3])       # City Library has Austen's book

# Librarians
Librarian.objects.create(name="Alice", library=lib1)
Librarian.objects.create(name="Bob", library=lib2)

print("✅ Sample data populated successfully.")


author_name = "George Orwell"

authors = Author.objects.filter(name=author_name)
for author in authors:
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books_by_author:
        print(f" - {book.title}")

# List all books in a library
library_name = "Central Library"
lib = Library.objects.get(name=library_name)
print(f"\nBooks in library '{lib.name}':")
for b in lib.books.all():
    print(f"- {b.title}")

# Retrieve the librarian for a library
print(f"\nLibrarian for library '{lib.name}': {lib.librarian.name}")

# ✅ Retrieve all staff (librarian queryset)
print("\nAll staff (librarians):")
staffqs = Librarian.objects.all()
for staff in staffqs:
    print(f"- {staff.name} (manages {staff.library.name})")