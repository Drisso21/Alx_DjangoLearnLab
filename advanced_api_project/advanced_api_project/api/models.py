from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey("Author", related_name='books' , on_delete=models.CASCADE)

    def __str__(self):
        return f"book {self.title} puplished {self.publication_year} by {self.author}"
    