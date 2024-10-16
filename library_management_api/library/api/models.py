
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


# CustomUserManager: A manager for the CustomUser model, responsible for creating user instances.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

    

class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'# Use email for authentication
    REQUIRED_FIELDS = ['username']# Required fields for user creation

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    



# Signal to create an authentication token when a new user is created
@receiver (post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
      Token.objects.create(user=instance)
       # Create a token only if the user was just created
      
'''
class Book(models.Model):
    Title = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    Isbn = models.CharField(max_length=13, unique=True)
    Published_Date = models.DateField(auto_now_add=True)
    Copies_Available = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class Transaction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True )
    return_date = models.DateTimeField(auto_now_add= True,null= True)

    def __str__(self):
        return f"{self.user.username} checked out {self.book.Title}"






#'''

from django.db import models
from django.contrib.auth.models import User


# Book: Represents a book in the library with its attributes.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField(auto_now_add=True)
    number_of_copies = models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.title




class LibraryUser(models.Model):# LibraryUser: Represents a user of the library, extending the CustomUser model.
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    date_of_membership = models.DateField(auto_now_add=True,null=True, blank=True)
    is_active = models.BooleanField(default=True)




class Transaction(models.Model):# Transaction: Represents a borrowing transaction in the library.
    user = models.ForeignKey(LibraryUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'book')
