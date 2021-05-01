from rest_framework import serializers

from .models import User, Post, Message
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'freinds']
        
class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Post
        fields = ['body', 'likes', 'author', 'timestamp'] 