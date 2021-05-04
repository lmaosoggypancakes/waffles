from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    #permission_classes = [permissions.IsAuthenticated]
@csrf_exempt
def update(request, id):
    post = Post.objects.get(id=id)
    if request.GET["ok"]:
        post.likes += 1
        post.save()
    else: 
        post.likes -= 1
        post.save()
    return JsonResponse({
        "message": "post updated."
    })