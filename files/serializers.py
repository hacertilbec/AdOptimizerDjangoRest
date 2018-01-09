from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import FileModel


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileModel
        #owner = serializers.ReadOnlyField(source='owner.username')
        fields = ("owner","f")

    def create(self, validated_data):
        return FileModel.objects.create(**validated_data)
