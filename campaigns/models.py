from django.contrib.auth.models import User
from django.db import models


class Campaign(models.Model):
    name = models.CharField(max_length=128)
    ctr = models.CharField(max_length=10)
    cr = models.CharField(max_length=10)
    keywords = models.TextField(max_length=500)
    status = models.CharField(max_length=10, default = "good")
    activation = models.CharField(max_length=10, default = "active")
    #author = models.ForeignKey(User)
