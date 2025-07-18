# Create a Book

```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
book
python
Copy
Edit
# Output:
<Book: 1984 (1949)>  # Book successfully created