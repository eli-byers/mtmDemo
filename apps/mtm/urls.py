from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^users$', views.users),
    url(r'^show/(?P<id>\d+)$', views.show),
]
