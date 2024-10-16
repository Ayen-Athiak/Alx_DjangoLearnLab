from rest_framework import viewsets, permissions
from .models import Book, CustomUser, Transaction
from .serializers import BookSerializer, UserSerializer, TransactionSerializer
from rest_framework.response import Response
from rest_framework import status



'''class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


    def list(self, request):
        """GET: List all books."""
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """GET: Retrieve a single book by ID."""
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """POST: Create a new book."""
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """PUT: Update an existing book."""
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """DELETE: Remove a book."""
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


'''

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Book, LibraryUser, Transaction
from .serializers import BookSerializer, LibraryUserSerializer, TransactionSerializer,UserSerializer
from datetime import datetime

# CustomUserViewSet: Handles CRUD operations for CustomUser instances.
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# BookViewSet: Handles CRUD operations for Book instances.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save()

class LibraryUserViewSet(viewsets.ModelViewSet):
    queryset = LibraryUser.objects.all()
    serializer_class = LibraryUserSerializer




# TransactionViewSet: Handles checkout and return actions for book transactions.
class TransactionViewSet(viewsets.ViewSet):
    def checkout(self, request, pk=None):
        user = request.user  # Correctly access the user object
        book = get_object_or_404(Book, pk=pk)
  
  
  # Check if the book has available copies
        if book.number_of_copies > 0:
            Transaction.objects.create(user=user, book=book)
            book.number_of_copies -= 1
            book.save()
            return Response({'status': 'book checked out'}, status=status.HTTP_200_OK)

        return Response({'status': 'no copies available'}, status=status.HTTP_400_BAD_REQUEST)

    def return_book(self, request, pk=None):
        user = request.user  # Correctly access the user object
        transaction = get_object_or_404(Transaction, pk=pk, user=user)

        transaction.return_date = datetime.now()
        transaction.save()

        book = transaction.book
        book.number_of_copies += 1
        book.save()

        return Response({'status': 'book returned'}, status=status.HTTP_200_OK)