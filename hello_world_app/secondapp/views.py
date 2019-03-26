from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
# Create your views here.
from .serializer import CitySerializer
from rest_framework import generics
from .models import City
from hello_world_app.users import permissions
from rest_framework import viewsets
from rest_framework.response import Response

class CityViewSet(ListModelMixin,
                    RetrieveModelMixin,
                    CreateModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = (permissions.IsAdmin)
    queryset = City.objects.all()
    serializer_class = CitySerializer
    