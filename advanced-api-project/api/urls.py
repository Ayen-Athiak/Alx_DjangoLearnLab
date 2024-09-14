from django.urls import path
from .views import BookListView, BookDetailView,BookCreateView,BookDeleteView,BookUpdateView,b

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/', BookCreateView.as_view(), name='book-list'),
    path('books/', BookUpdateView.as_view(), name='book-detail'),
    path('books/', BookDeleteView.as_view(), name='book-detail'),
]
