from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.create_mailing, name='create_mailing'),
    url(r'^tracking/(?P<uuid>[a-f0-9-]+)\.png$', views.track_open, name='track_open'),
]