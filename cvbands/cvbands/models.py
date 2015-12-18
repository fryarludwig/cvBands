from django.db import models
from django.db.models import Count


class Band(models.Model):
    class Meta:
        app_label = 'cvBands'
    # boring stuff
    username = models.CharField(max_length=30)
    bandHash = models.CharField(max_length=30)

    # about them
    name = models.CharField(max_length=30)
    bio = models.CharField(max_length=500)
    events = models.ForeignKey('Event')

    # external links
    facebook = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    spotify = models.CharField(max_length=150)
    bandcamp = models.CharField(max_length=150)
    youtube = models.CharField(max_length=150)
    itunes = models.CharField(max_length=150)


class Event(models.Model):
    class Meta:
        app_label = 'cvBands'
    # boring stuff
    username = models.CharField(max_length=30)
    bandHash = models.CharField(max_length=30)

    # about them
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    bands = models.ForeignKey('Band')
    date = models.DateTimeField()
    location = models.CharField(max_length=150)

    # external links
    facebook = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    spotify = models.CharField(max_length=150)
    bandcamp = models.CharField(max_length=150)
    youtube = models.CharField(max_length=150)
    itunes = models.CharField(max_length=150)

class Graphic(models.Model):
    class Meta:
        app_label = 'cvBands'
    url = models.CharField(max_length=150)
    caption = models.CharField(max_length=150)
    band = models.ForeignKey('Band')
    event = models.ForeignKey('Event')

class Video(models.Model):
    class Meta:
        app_label = 'cvBands'
    url = models.CharField(max_length=150)
    caption = models.CharField(max_length=150)
    band = models.ForeignKey('Band')
    event = models.ForeignKey('Event')

class Album(models.Model):
    class Meta:
        app_label = 'cvBands'
    date = models.DateField()
    songs = models.ForeignKey('Song')
    coverArt = models.ForeignKey('Graphic')
    purchaseUrl = models.CharField(max_length=150)
    band = models.ForeignKey('Band')

class Song(models.Model):
    class Meta:
        app_label = 'cvBands'
    url = models.CharField(max_length=150)
    playCount = models.PositiveIntegerField()
    band = models.ForeignKey('Band')
    album = models.ForeignKey('Album')

