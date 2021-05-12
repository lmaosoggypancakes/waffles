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
class UserViewSet(viewsets.ModelViewSet):
    """
    Model view set provided by DRF that allows us to easily handle GET/POST requests.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("-timestamp")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    """
    Users who are not authenticated are allowed to view posts, but only those who provide
    the corrent authentication can send POST requests.
    """
    def create(self, request):
        post = Post(
            body = request.data["body"],
            author = request.user,
            likes = 0
        ).save()
        return Response({"message": "Your post has been saved"})
@csrf_exempt
def update(request, id):
    """
    Updates the number of likes based on it's respective post.
    """
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
@api_view(["GET", "PUT"])
@permission_classes([IsAuthenticated])
def friends(request):
    """
    Serializes all friends of the request.user object. If a PUT request, updates a user's friend list.
    """
    if request.method == "GET":
        return Response(request.user.serialize_freinds())
    else: 
        request.user.freinds.add(User.objects.get(username=request.data["username"]))
        return Response({
            "Freinds list updated!"
        })