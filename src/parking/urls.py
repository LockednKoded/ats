from django.conf.urls import url

from .views import (parking_details, search_vehicle, add_vehicle, delete_vehicle, update_spots)

app_name = "parking"

urlpatterns = [
    url(r'^$', parking_details, name='details'),
    url(r'^search/', search_vehicle, name='search'),
    url(r'^add/', add_vehicle, name='add'),
    url(r'^(?P<pk>[a-z,A-Z,0-9]+)/delete/$', delete_vehicle, name='delete'),
    url(r'^spots$', update_spots, name='update_spots'),
]
