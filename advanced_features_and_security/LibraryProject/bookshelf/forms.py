from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text='Enter the book title.')
    author = forms.CharField(max_length=100, help_text='Enter the book author.')
    publication_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)), help_text='Enter the publication date.')
    isbn = forms.CharField(max_length=13, min_length=10, help_text='Enter the book ISBN number.')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date','isbn' ]

    def clean_isbn(self):
        isbn = self.cleaned_data.get('author')
        if not isbn.isdigit():
            raise forms.ValidationError("ISBN must be numeric.")
        return isbn
