import os
import django
from models import author, book, library, librarian


#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
#django.setup()


# Authors
a1 = author.objects.create(name="George Orwell")
a2 = author.objects.create(name="Jane Austen")

# Books
b1 = book.objects.create(title="1984", author=a1)
b2 = book.objects.create(title="Animal Farm", author=a1)
b3 = book.objects.create(title="Pride and Prejudice", author=a2)

# Libraries
lib1 = library.objects.create(name="Central Library")
lib2 = library.objects.create(name="City Library")

# Assign books to libraries
lib1.books.set([b1, b2])   # Central Library has Orwell's books
lib2.books.set([b3])       # City Library has Austen's book

# Librarians
librarian.objects.create(name="Alice", library=lib1)
librarian.objects.create(name="Bob", library=lib2)

print("✅ Sample data populated successfully.")
george = author.objects.get(name="George Orwell")
print(f"Books by {george.name}:")
for b in george.books.all():
    print(f"- {b.title}")

# List all books in a library
lib = library.objects.get(name="Central Library")
print(f"\nBooks in library '{lib.name}':")
for b in lib.books.all():
    print(f"- {b.title}")

# Retrieve the librarian for a library
print(f"\nLibrarian for library '{lib.name}': {lib.librarian.name}")

# ✅ Retrieve all staff (librarian queryset)
print("\nAll staff (librarians):")
staffqs = librarian.objects.all()
for staff in staffqs:
    print(f"- {staff.name} (manages {staff.library.name})")