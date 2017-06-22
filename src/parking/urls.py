from django.conf.urls import url

from .views import (parking_details,)

urlpatterns = [
    url(r'^$', parking_details),
]