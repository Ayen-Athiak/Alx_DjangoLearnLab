
from django.urls import  path
from . import views

urlpatterns = [
  
    path('', views.list_books, name = 'list_path'),
    path('', views.LibraryDetailView.as_view,'library_detail'),
]