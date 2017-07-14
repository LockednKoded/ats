from django.conf.urls import url
from .views import test_view, search_worker, assign_worker

app_name = "maintenance"

urlpatterns = [

    #  /maintenance/
    url(r'^$', test_view, name='test-view'),
    url(r'^search$', search_worker, name='search_worker'),
    url(r'^assign$', assign_worker, name='assign_worker'),
]
