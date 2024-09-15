from django_filters.rest_framework import DjangoFilterBackend,filters
from .models import Book
from django_filters.rest_framework import DjangoFilterBackend



class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='icontains')
    publication_year = filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
