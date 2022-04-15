from django import forms
from .models import Book, Book,Comment
from .snippets import choices

class BookCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter title'}))
    author = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Author Name'}))
    categories = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Categories separated by comma. Example: Thriller, Drama, Novel'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    price = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Book Price'}))
    details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Book
        fields = ['title','image','author','categories','price','details']
