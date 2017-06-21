from django.conf.urls import url

from .views import (flight_details,)

urlpatterns = [
    url(r'^$', flight_details),
]