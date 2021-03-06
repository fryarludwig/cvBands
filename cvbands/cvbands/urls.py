"""cvbands URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.conf.urls import include
from cvbands.views import (auth, main_page, discover, manage_band, view_event,
    view_band, discover)

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^auth/$', auth, name='auth'),
    url(r'^$', main_page, name='main_page'),
    url(r'^home/$', main_page, name='main_page'),
    url(r'^manage_band/$', manage_band, name='manage_band'),
    url(r'^view_band/$', view_band, name='view_band'),
    url(r'^view_event/$', view_event, name='view_event'),
    url(r'^view_band/$', view_band, name='view_band'),
    url(r'^discover/$', discover, name='discover'),
]
