from django.conf.urls import url
from . import views
urlpatterns = [
    #/baggage/
    url(r'^$', views.index, name='index'),
]