from django.db import models



class Author(models.Model):

    """
    Represents an author in the system.

    Attributes:
        name (CharField): The name of the author.
"""


    name = models.CharField(max_length=100)


class Book(models.Model):

    """
    Represents a book in the system.

    Attributes:
        title (CharField): The title of the book.
        publication_year (PositiveIntegerField): The year the book was published.
        author (ForeignKey): A reference to the Author who wrote the book.
"""





    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
