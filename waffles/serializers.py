from rest_framework import serializers

from .models import User, Post, Message
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        
class PostSerializer(serializers.ModelSerializer): 
    author = UserSerializer()
    class Meta:
        model = Post
        fields = ['body', 'likes', 'author', 'timestamp', 'id'] 