### Searching
You can search books using the `search` query parameter:
- `search`: Search in title and author fields (e.g., `GET /books/?search=wizard`)


### Ordering
You can order books using the `ordering` query parameter:
- `ordering`: Order by specific field (e.g., `GET /books/?ordering=title`)
- Prefix with `-` for descending order (e.g., `GET /books/?ordering=-publication_year`)


### Filtering
You can filter books using query parameters:
- `title`: Filter by book title (e.g., `GET /books/?title=Harry Potter`)
- `author`: Filter by author name (e.g., `GET /books/?author=J.K. Rowling`)
- `publication_year`: Filter by publication year (e.g., `GET /books/?publication_year=2000`)



##
### unitest


### Testing API Endpoints

#### Overview

This document outlines the tests for CRUD operations, filtering, searching, ordering, and permissions for the Book API endpoints.

#### Test Cases

1. **Create Book**: Tests POST requests to create a new book.
2. **Read Book**: Tests GET requests to retrieve a single book by ID.
3. **Update Book**: Tests PUT requests to update an existing book.
4. **Delete Book**: Tests DELETE requests to remove a book.
5. **Filter Books**: Tests filtering by title.
6. **Search Books**: Tests searching by title.
7. **Ordering Books**: Tests ordering by publication year.
8. **Permissions**: Tests access control for authenticated and unauthenticated users.



