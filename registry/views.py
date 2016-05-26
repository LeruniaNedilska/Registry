#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render


def registry(request):
    person = ['Путин', 'Мишутин']
    return render(request, "registry.html", {'person': person})


def search(request):
    if request.method == 'GET':
        return render(request, "search.html")
    else:
        s = request.POST.get("search")
        return render(request, "results.html", {'person': s})


def requests(request):
    if request.method == 'GET':
        return render(request, "request.html")
    else:
        s = request.POST.get("search")
        return render(request, "request_results.html")
