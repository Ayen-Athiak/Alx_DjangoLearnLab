from relationship_app.models import Author,Book,Librarian,Library



#Query all books by a specific author

# Query all books by a specific author using objects.filter()
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        print(f"No author found with the name '{author_name}'")
        return []

# List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'")
        return []

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian found for the library '{library_name}'")
        return None

if __name__ == "__main__":
    # Example usage
    author_name = 'J.K. Rowling'
    print(f"Books by Author '{author_name}':")
    books = get_books_by_author(author_name)
    if books:
        for book in books:
            print(book.title)
    else:
        print(f"No books found for author '{author_name}'.")

    library_name = 'Central Library'
    print(f"\nBooks in Library '{library_name}':")
    books = get_books_in_library(library_name)
    if books:
        for book in books:
            print(book.title)
    else:
        print(f"No books found in library '{library_name}'.")

    print(f"\nLibrarian for Library '{library_name}':")
    librarian = get_librarian_for_library(library_name)
    if librarian:
        print(librarian.name)
    else:
        print(f"No librarian found for library '{library_name}'.")
