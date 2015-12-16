from django.db import models
from django.db.models import Count


class imageModel(models.Manager):
    class Meta:
        app_label = 'cvBands'
    url = ""
    caption = ""
    band = ""
    event = ""


class videoModel(models.Manager):
    class Meta:
        app_label = 'cvBands'
    url = ""
    caption = ""
    band = ""
    event = ""


class songModel(models.Manager):
    class Meta:
        app_label = 'cvBands'
    url = ""
    playCount = ""
    band = ""
    album = ""


class albumModel(models.Manager):
    class Meta:
        app_label = 'cvBands'
    date = ""
    songs = []
    coverArt = ""
    purchaseUrl = ""
