from django.conf.urls import url
from .views import *

app_name = "baggage_handling"


urlpatterns = [
    #/baggage/
    url(r'^$', index, name='index'),

    # Baggage Options:

    # Homepage for baggage, showing a list of all baggage, /baggage_handling/list/
    url(r'^list$', list_baggages, name="list-baggage"),

    # Option to add new baggage, /baggage_handling/add/
    url(r'^add/$', add_baggage, name="add-baggage"),


    # Option to view baggage details, /baggage_handling/5
    url(r'^(?P<pk>[0-9]+)$', view_baggage, name="view-baggage"),

    # Option to delete flight, /baggage_handling/5/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', delete_baggage, name="delete-baggage"),

    # Option to edit baggage details, /baggage_handling/5/edit
    url(r'^(?P<pk>[0-9]+)/edit/$', edit_baggage, name="edit-baggage"),
]