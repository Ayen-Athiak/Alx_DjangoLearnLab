from django.shortcuts import render
from .serializers import BookSerializer,AuthorSerializer
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissionsOrAnonReadOnly
from .models import Book,Author
from rest_framework.generics import (
    ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,
)

# Create your views here.
from rest_framework.permissions import IsAuthenticated, AllowAny

 
class BookCreateAPIView(generices.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Allow unauthenticated users to list books

class BookUpdateAPIView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users

class BookDestroyAPIView (generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookDetailAPIView(generics.DetailAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
