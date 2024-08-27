from typing import Any
from django.shortcuts import render

from django.views.generic import DetailView
from .models import Book,Librarian,Library,Author

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    content = {'books' : books}
    return render(request, 'list_books.html', content)




class LibraryDetailView(DetailView):
    
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'  
    
    def get_context_data(self, **kwargs):
        """Add additional context data specific to the library."""
        context = super().get_context_data(**kwargs)
        return context

    
    
    
    


    

