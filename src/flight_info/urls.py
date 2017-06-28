from django.conf.urls import url
from .views import *

app_name = "flight_info"

urlpatterns = [

    # Flight Options:

    # Homepage for flights, showing a list of all scheduled flights, /flights/
    url(r'^$', list_flights, name="list-flights"),

    # Option to add new flights, /flights/add/
    url(r'^add/$', add_flight, name="add-flight"),

    # Option to view flight details, /flights/5/
    url(r'^(?P<pk>[0-9]+)/$', view_flight, name="view-flight"),

    # Option to delete flight, /flights/5/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', delete_flight, name="delete-flight"),

    # Option to edit flight details, /flights/5/edit
    url(r'^(?P<pk>[0-9]+)/edit/$', edit_flight, name="edit-flight"),

    # Crew Options:

    # Option to view all crew/pilots, /flights/crew
    url(r'^crew/$', list_crew, name="list-crew"),

    # Option to add crew, /flights/crew/add
    url(r'^crew/add/$', add_crew, name="add-crew"),

    # Option to view crew details, /flights/crew/5
    url(r'^crew/(?P<pk>[0-9]+)/$', view_crew, name="view-crew"),

    # Option to delete crew, /flights/crew/5/delete
    url(r'^crew/(?P<pk>[0-9]+)/delete/$', delete_crew, name="delete-crew"),

    # Option to edit crew details, /flights/crew/5/edit
    url(r'^crew/(?P<pk>[0-9]+)/edit/$', edit_crew, name="edit-crew"),

]