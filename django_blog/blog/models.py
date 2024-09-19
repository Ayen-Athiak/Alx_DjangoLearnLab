from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=callable)




   
    


