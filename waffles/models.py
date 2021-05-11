from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    freinds = models.ManyToManyField('self', symmetrical=True)
    def serialize(self):
        return {
            'username': self.username,
            'email': self.email,
            "name": {
                "first": self.first_name,
                'last': self.last_name
            },
            "id": self.id
        }
    def serialize_freinds(self):
        return [user.serialize() for user in self.freinds.all()] 

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
    def serialize(self):
        return {
            "body": self.content,
            "to": self.user_to.serialize(),
            "from": self.user_from.serialize(),
            "timestamp": self.timestamp.strftime("%A %I:%M %p")
        }



