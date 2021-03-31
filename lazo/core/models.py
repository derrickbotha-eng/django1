# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from time import time 
from datetime import datetime, timedelta, tzinfo
# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):

    topic = models.ForeignKey(Topic)
    text = models.TextField(default='')
    dateTime = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        return self.text[:50] + "..."

        
    