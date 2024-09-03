from bookshelf.models import Book



# Retrieve the book
book = Book.objects.get(title='1984')
print(book.title, book.author, book.publication_year)  # Expected output: 1984 George Orwell 1949





# Security Measures

## Security Settings in `settings.py`

- **DEBUG**: Set to `False` to prevent exposing debug information in production.
- **CSP (Content Security Policy)**: Configured to allow scripts and styles only from trusted sources to mitigate XSS attacks.
- **Secure Cookies**: `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE` set to `True` to ensure cookies are sent over HTTPS.
- **XSS Filter**: Enabled via `SECURE_BROWSER_XSS_FILTER`.
- **Frame Options**: Set to `'DENY'` to prevent clickjacking attacks.
- **Content Type Sniffing**: Disabled via `SECURE_CONTENT_TYPE_NOSNIFF`.

## Form and Input Validation

- All forms include CSRF tokens to protect against CSRF attacks.
- User inputs are validated and sanitized using Django forms to prevent SQL injection and other vulnerabilities.


Testing Approach
1. Manual Testing:

CSRF Protection Testing:

Attempt to submit forms without a CSRF token to ensure they are rejected.
Verify that the CSRF token is present in all forms by inspecting the HTML source code.
XSS Protection Testing:

Try to inject malicious scripts into form inputs and see if they are properly sanitized and not executed.
Test various input fields to ensure they handle and escape dangerous characters correctly.
