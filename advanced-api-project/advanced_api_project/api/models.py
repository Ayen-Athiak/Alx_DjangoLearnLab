from django.db import models

# Create your models here.


class Author(models.Model):
    """
    Represents an author with a name.

    Attributes:
        name (str): The name of the author.
"""



    name = models.CharField(max_length=100)


class Book(models.Model):  
    """
    Represents a book written by an author.

    Attributes:
        title (str): The title of the book.
        publication_year (int): The year the book was published.
        author (ForeignKey): The author who wrote the book.
"""




    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
