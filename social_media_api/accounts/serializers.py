# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'bio', 'profile_picture')

class RegistrationSerializer(serializers.ModelSerializer):
    # Include a password field with write-only access
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user and set the password
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        # Create a token for the new user
        Token.objects.create(user=user)
        return user
