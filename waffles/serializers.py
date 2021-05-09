from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Post, Message
class UserSerializer(serializers.ModelSerializer):
    def validate_password(self, value: str) -> str:
        return make_password(value)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        
class PostSerializer(serializers.ModelSerializer): 
    author = UserSerializer()
    class Meta:
        model = Post
        fields = ['body', 'likes', 'author', 'timestamp', 'id'] 