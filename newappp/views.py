from django.shortcuts import render

# Create your views here.
from .serializers import PostSerializer
from rest_framework import generics
from .models import Post

class ListCreate(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
