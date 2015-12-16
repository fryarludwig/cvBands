from django.db import models
from django.db.models import Count


class Band(models.Manager):
    class Meta:
        app_label = 'cvBands'
    # boring stuff
    username = models.CharField(max_length=30)
    bandHash = models.CharField(max_length=30)

    # about them
    name = models.CharField(max_length=30)
    bio = models.CharField(max_length=500)
    event = models.ForeignKey(Event, related_name='Event')

    # external links
    facebook = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    spotify = models.CharField(max_length=150)
    bandcamp = models.CharField(max_length=150)
    youtube = models.CharField(max_length=150)
    itunes = models.CharField(max_length=150)


class Event(models.Manager):
    class Meta:
        app_label = 'cvBands'
    # boring stuff
    username = models.CharField(max_length=30)
    bandHash = models.CharField(max_length=30)

    # about them
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    bands = models.ForeignKey(Band, related_name='Band')
    date = models.DateTimeField()
    location = models.CharField(max_length=150)

    # external links
    facebook = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    spotify = models.CharField(max_length=150)
    bandcamp = models.CharField(max_length=150)
    youtube = models.CharField(max_length=150)
    itunes = models.CharField(max_length=150)
