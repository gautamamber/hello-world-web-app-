from django.shortcuts import render
from .models import FileUpload
from .serializers import FileSerializer
# Create your views here.
from rest_framework import viewsets
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)


class FileViewSet(ListModelMixin,
                    RetrieveModelMixin,
                    CreateModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    viewsets.GenericViewSet):
    
    queryset = FileUpload.objects.all()
    serializer_class = FileSerializer
    