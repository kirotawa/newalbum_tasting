#!/usr/bin/env python
# encoding: utf-8
     
# from base.forms import LoginForm
from django.conf.urls import patterns, include, url 
#from django.contrib.auth.views import login
             
urlpatterns = patterns('core.views',
    url(r'^/?$', 'main', name="main"),
    url(r'^index/?$', 'main', name="main"),
)
