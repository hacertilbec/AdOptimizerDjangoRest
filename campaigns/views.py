from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .models import Campaign
from .serializers import CampaignSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
