from django.db import models

from django.contrib.auth.models import AbstractUser,BaseUserManager,AbstractBaseUser
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()






class usermanager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password = None):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_staff = True
        
        user.save(using=self._db)
        return user
    



class CustomUser (AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True,verbose_name="D.O.B")
    profiles_photo = models.ImageField(profiles_photo= "/image",null=False,blank=True)
    company_name = models.CharField(blank=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = usermanager()

    def __str__(self):
        return self.email

