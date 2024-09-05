from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
>>>>>>> 4426c1bee6525b3a7279a2554af64684bd8720bd
