from django.conf.urls import url

from .views import *

app_name = 'terminal_info'

urlpatterns = [
    url(r'^$', terminal_info),
    url(r'^terminal_1/$', terminal_1_view, name='terminal_1'),
    url(r'^terminal_3/$', terminal_1_view_1, name='terminal_3'),
]