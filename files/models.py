# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class FileModel(models.Model):
    owner =  models.CharField(max_length=128, default = "hacer")
    f = models.FileField(upload_to='uploads/')
