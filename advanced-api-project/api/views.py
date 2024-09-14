from django.shortcuts import render
from .serializers import BookSerializer,AuthorSerializer
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissionsOrAnonReadOnly
from .models import Book,Author
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,ListCreateAPIView,
)

# Create your views here.
from rest_framework.permissions import IsAuthenticated, AllowAny

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Allow unauthenticated users to list books

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users

