from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import json
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = [permissions.IsAuthenticated]

def update(request, id):
    post = Post.objects.get(id=id)
    data = json.loads(request.body)
    if data["like"]:
        post.likes += 1
        post.save()
    else: 
        post.likes -= 1
        post.save()
