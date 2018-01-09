# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .models import FileModel
from .serializers import FileSerializer

from rest_framework.parsers import MultiPartParser, FormParser


class FileViewSet(viewsets.ModelViewSet):
    queryset = FileModel.objects.all()
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser, FormParser,)


    def perform_create(self, serializer, format=None):
        file = self.request.data.get('file', False)
        serializer.save(
            owner=serializer.validated_data.get('owner'),
            f=file
            )
