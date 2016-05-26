#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
import registry.views as views

admin.site.site_header = "Очищення влади"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main', views.registry, name='registry'),
    url(r'^search', views.search, name='search'),
    url(r'^request', views.requests, name='requests')
]
