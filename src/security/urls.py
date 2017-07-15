from django.conf.urls import url

from .views import (security_details,)

urlpatterns = [
    url(r'^$', security_details),
]