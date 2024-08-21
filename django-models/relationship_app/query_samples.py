from relationship_app.models import Author,Book,Librarian,Library


books = Book.objects.filter(author=author)

library = Library.objects.get(name=library_name)

librarian = library.librarian