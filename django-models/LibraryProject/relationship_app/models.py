from django.db import models

class author(models.Model):
    name = models.CharField(max_length=100)


class book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(author, on_delete=models.CASCADE, related_name='books')

class library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(book, related_name='libraries')

class librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(library, on_delete=models.CASCADE, related_name='librarian')