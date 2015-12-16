from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import ListView
from django.template.defaultfilters import slugify
from .models import Band, Event, Graphic, Video, Song, Album
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView
from django.http import HttpResponse


def auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
        else:
            return redirect('/login')
    else:
        return redirect('/login')


def MainPage(request):
    return render(request, 'home.html', {})

def Discover(request):
    return render(request, 'discover.html', {})

def ViewBand(request):
    return render(request, 'view_band.html', {'band': requests.band})

