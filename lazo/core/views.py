# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Topic

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def topics(request):
    #show all topics

    topics = Topic.objects.order_by('dateTime')
    context = {'topics':topics}

    return render(request, 'core/topics.html', context)

