
from rest_framework import serializers
from rest_framework import status
from models import (
    Book,Author,
)




class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    This serializer handles:
        - Serializing all fields of the Book model.
        - Custom validation for the publication_year field to ensure it is not in the future.
"""



    class Meta:
        model = Book
        fields = ('__all__')


    def validate_publication_year(self, value):
        """
        Validate that the publication year is not in the future.

        Args:
            value (int): The year to validate.

        Returns:
            int: The validated year if it is not in the future.

        Raises:
            serializers.ValidationError: If the year is in the future.
"""
       
       
       
       
       
        import datetime
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value    
        
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    This serializer handles:
        - Serializing the name field of the Author model.
        - Including a nested representation of related books using the BookSerializer.
    """



    relation = BookSerializer(many = True)
    class Meta:
            model = Author
            fields = ['name','relation']