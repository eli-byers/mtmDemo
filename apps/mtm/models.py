from __future__ import unicode_literals

from django.db import models

class Interest(models.Model):
    name = models.CharField(max_length=30)

class User(models.Model):
    name = models.CharField(max_length=30)
    interests = models.ManyToManyField(Interest)


# Create your models here.
