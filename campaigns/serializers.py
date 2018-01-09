from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Campaign


class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campaign
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ("name","ctr","cr","keywords","status","activation")
