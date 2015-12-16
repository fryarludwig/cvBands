from django.db import models
from django.db.models import Count


class Graphic(models.Manager):
    class Meta:
        app_label = 'cvBands'
    url = models.CharField(max_length=150)
    caption = models.CharField(max_length=150)
    band = models.ForeignKey(Band, related_name='Band')
    event = models.ForeignKey(Event, related_name='Event')

class Video(models.Manager):
    class Meta:
        app_label = 'cvBands'
    url = "models.CharField(max_length=150)
    caption = models.CharField(max_length=150)
    band = models.ForeignKey(Band, related_name='Band')
    event = models.ForeignKey(Event, related_name='Event')


class Song(models.Manager):
    class Meta:
        app_label = 'cvBands'
    url = models.CharField(max_length=150)
    playCount = models.PositiveIntegerField()
    band = models.ForeignKey(Band, related_name='Band')
    album = models.ForeignKey(Album, related_name='Album')


class Album(models.Manager):
    class Meta:
        app_label = 'cvBands'
    date = models.DateField()
    songs = models.ForeignKey(Song, related_name='Song')
    coverArt = models.ForeignKey(Graphic, related_name='Graphic')
    purchaseUrl = models.CharField(max_length=150)
    band = models.ForeignKey(Band, related_name='Band')
