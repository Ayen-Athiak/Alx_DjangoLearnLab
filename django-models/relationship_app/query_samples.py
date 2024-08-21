from relationship_app.models import Author,Book,Librarian,Library

# Query all books by a specific author
def get_books_by_author(author):
    author = Author.objects.filter(author = author)
    books = author.books.all()
    return books

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return librarian

if __name__ == "__main__":
    # Example usage
    print("Books by Author 'J.K. Rowling':")
    books = get_books_by_author('J.K. Rowling')
    for book in books:
        print(book.title)

    print("\nBooks in Library 'Central Library':")
    books = get_books_in_library('Central Library')
    for book in books:
        print(book.title)

    print("\nLibrarian for Library 'Central Library':")
    librarian = get_librarian_for_library('Central Library')
    print(librarian.name)
