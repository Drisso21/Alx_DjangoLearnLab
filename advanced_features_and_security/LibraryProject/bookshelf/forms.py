from django import forms
from .models import Book
from .forms import ExampleForm

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


class BookSearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")
