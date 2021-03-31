from django.conf.urls import url

from . import views

urlpatterns = [
    #home page
    url(r'^$', views.home, name='home'),

    #page to show all topics
    url(r'^topics/$', views.topics, name="topics"),

    #url for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name="topic")


]


