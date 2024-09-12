from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Song(models.Model):

    name = models.CharField(max_length=200)
    song_image = models.ImageField(upload_to='covers/', default='default.jpg')
    singer = models.CharField(max_length=200)
    song_file = models.FileField(upload_to='songs/')

    def __str__(self):
        return self.name
