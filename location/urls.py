from django.conf.urls import patterns, url
from .views import index, place_index

urlpatterns = [
    url(r'^$', index, name = "index"),
    url(r'^location/(?P<place_id>[0-9]+)/$', place_index, name = "place_index"),
]
