from django.shortcuts import render

# Create your views here.
from .serializers import PostSerializer
from rest_framework import generics
from .models import Post
from rest_framework.response import Response
from rest_framework import viewsets
class ListCreatePost(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)