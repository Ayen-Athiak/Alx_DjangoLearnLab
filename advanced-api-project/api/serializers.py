from models import Book,Author


from rest_framework import serializers



class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    Serializes the fields of the Book model and includes validation to ensure the publication_year is not in the future.

    Fields:
        title (str): The title of the book.
        publication_year (int): The year the book was published.
        author (AuthorSerializer): Details of the author who wrote the book.
    """


    class Meta:
        model = Book
        fields = '__all__'



    def validate(self, data):
        """
        Check that the publication_year is not in the future.
        """
        publication_year = data.get('publication_year')
        
        if publication_year and publication_year > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        
        return data   

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    Serializes the fields of the Author model and includes nested serialization of related books.

    Fields:
        name (str): The name of the author.
        books (list): A list of books written by the author, serialized using BookSerializer.
    """



    relation = BookSerializer(many = True read_only =True)   
   
   
    class Meta:
        model = Author
        fields = ['name','relation']




