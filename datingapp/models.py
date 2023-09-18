from django.db import models

# Create your models here.
from user.models import *


class cumpuses(models.Model):
    name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    def __str__(self):
        return self.name