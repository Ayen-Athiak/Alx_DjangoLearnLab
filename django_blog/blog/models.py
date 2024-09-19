from django.db import models

# Create your models here.


class User(models.Model): 
    username = models.CharField(max_length=255)
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=callable)




   
    


