from relationship_app.models import Author,Book,Librarian,Library


books = Book.objects.filter(author=author)
print(books)

library = Library.objects.get(name=library_name)
print(library)

librarian = library.librarian
print(librarian)