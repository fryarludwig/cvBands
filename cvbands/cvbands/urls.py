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
from django.contrib import admin

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^auth/$', auth, name='auth'),
    url(r'^$', MainPage.as_view(), name='home'),


    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^auth/$', auth, name='auth'),
    url(r'^submit_link/$', submit_link, name='submit_link'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^accounts/register/$', register, name='register'),
    url(r'^r/$', subreddit_view, name='subreddits'),
    url(r'^r/(?P<sub>[\w]+)/$', subreddit_selector, name='subreddits'),
    url(r'^discuss/(?P<link>[\w-]+)/$', link_discuss, name='links'),
    url(r'^v/l/(?P<link_id>[\w-]+)/$', vote_link, name='links'),
    url(r'^v/c/(?P<comment_id>[\w-]+)/$', vote_comment, name='links'),
]
