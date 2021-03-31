# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Topic, Entry

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def topics(request):
    #show all topics

    topics = Topic.objects.order_by('dateTime')
    context = {'topics':topics}

    return render(request, 'core/topics.html', context)



def topic(request, topic_id):

    #show an entry of a topic

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-dateTime')
    context = {'topic':topic, 'entries': entries}
    return render(request, 'core/topic.html', context)

