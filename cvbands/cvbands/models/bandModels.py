from django.db import models
from django.db.models import Count


class bandModel(models.Manager):
    class Meta:
        app_label = 'cvBands'
    # boring stuff
    bandId = ""
    username = ""
    bandHash = ""

    # about them
    name = ""
    bio = ""
    genres = ""
    images = ""
    videos = ""
    songs = ""
    albums = ""

    # external links
    facebook = ""
    instagram = ""
    spotify = ""
    bandcamp = ""
    youtube = ""
    itunes = ""

    # Their activity
    events = ""
    posts = ""
    topTracks = ""
