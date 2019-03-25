from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from .serializer import CitySerializer
from rest_framework import generics
from .models import City
from rest_framework import viewsets
from rest_framework.response import Response

class CityViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = City.objects.all()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data)
