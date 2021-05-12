from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Post, Message
class UserSerializer(serializers.ModelSerializer):
    def validate_password(self, value: str) -> str:
        """
        Hashes the password provided on POST requests prior to saving.
        """
        return make_password(value)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password'] # we can't serialize freinds recursively because it would go in an infinite loop. (friendships are birectional here)
        
class PostSerializer(serializers.ModelSerializer): 
    author = UserSerializer() # serialize a foreign key to the author
    class Meta:
        model = Post
        fields = ['body', 'likes', 'author', 'timestamp', 'id'] 