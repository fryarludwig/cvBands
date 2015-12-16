from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
#from .models.bandModels import Band, Event, Graphic, Video, Song, Album
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
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


def main_page(request):
    return render(request, 'home.html', {})

def discover(request):
    return render(request, 'discover.html', {}) #

def view_band(request):
    return render(request, 'view_band.html', {}) # {'band': requests.band})


def manage_band(request):
    return render(request, 'manage_band.html', {}) # {'band': requests.band})


def view_event(request):
    return render(request, 'view_event.html', {}) # {'event': requests.event})

