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
from .serializer import PersonSerializer
from rest_framework import generics
from .models import Person

from rest_framework import viewsets
from rest_framework.response import Response

class PersonViewSet(ListModelMixin,
                    RetrieveModelMixin,
                    CreateModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    viewsets.GenericViewSet):
    
    queryset =Person.objects.all()
    serializer_class = PersonSerializer
