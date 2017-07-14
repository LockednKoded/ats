from django.conf.urls import url

from .views import (terminal_info,)

urlpatterns = [
    url(r'^$', terminal_info),
]