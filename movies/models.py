from django.db import models
from django.utils import timezone

class Studio(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=50)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    releaseDate = models.DateField()
    rentDate = models.DateField(default=timezone.now())
    studio = models.ForeignKey(Studio,on_delete=models.CASCADE)
