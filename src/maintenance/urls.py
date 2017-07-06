from django.conf.urls import url
from .views import *

app_name = "maintenance"

urlpatterns = [

    #  /maintenance/
    url(r'^$', test_view, name="test-view"),
]