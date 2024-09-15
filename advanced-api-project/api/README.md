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
