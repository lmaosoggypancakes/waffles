from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.response import Response
SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def add_freind(request):
    request.user.freinds.add(User.objects.get(username=request.data["username"]))
    return Response({
        "message": "Freinds list updated!"
    })
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("-timestamp")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def create(self, request):
        post = Post(
            body = request.data["body"],
            author = request.user,
            likes = 0
        ).save()
        return Response({"message": "Your post has been saved"})
@csrf_exempt
def update(request, id):
    post = Post.objects.get(id=id)
    if request.GET["ok"] == "true":
        post.likes += 1
        post.save()
    else: 
        post.likes -= 1
        post.save()
    return JsonResponse({
        "message": "post updated."
    })
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def freinds(request):
    return Response(request.user.serialize_freinds())