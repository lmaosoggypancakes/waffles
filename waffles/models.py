from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    freinds = models.ManyToManyField('self', symmetrical=False)


class Post(models.Model):
    body = models.TextField()
    author = models.ForeignKey('user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField() # just a numerical amount of likes for now
    
class Message(models.Model):
    content = models.TextField()
    user_from = models.ForeignKey('user', on_delete=models.CASCADE, related_name="_from")
    user_to = models.ForeignKey('user', on_delete=models.CASCADE, related_name="_to")
    timestamp = models.DateTimeField(auto_now_add=True)
    
