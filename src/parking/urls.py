from django.conf.urls import url

from .views import (parking_details, search)

urlpatterns = [
    url(r'^$', parking_details, name='details'),
    url(r'^search/', search, name='search'),
]
