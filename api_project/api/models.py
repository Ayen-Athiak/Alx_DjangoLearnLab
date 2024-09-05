from django.db import models

# Create your models here.
<<<<<<< HEAD
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    
=======

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField()
    

 
>>>>>>> 4426c1bee6525b3a7279a2554af64684bd8720bd
