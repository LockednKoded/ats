from django.conf.urls import url
from .views import *

app_name = "flight_info"

urlpatterns = [

    # Flight Options:

    # Homepage for flights, showing a list of all scheduled flights, /flights/   #done view
    url(r'^$', list_flights, name="list-flights"),

    # Option to add new flights, /flights/add/                   #done view
    url(r'^add/$', add_flight, name="add-flight"),

    # Option to view flight details, /flights/5/                    #done view
    url(r'^(?P<pk>[0-9]+)/$', view_flight, name="view-flight"),

    # Option to delete flight, /flights/5/delete/                       #done view
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

    # Airline Options:

    # Option to view all airlines, /flights/airlines
    url(r'^airlines/$', list_airlines, name="list-airlines"),

    # Option to add airlines, /flights/airlines/add
    url(r'^airlines/add/$', add_airlines, name="add-airlines"),

    # Option to view airline details, /flights/airlines/5
    url(r'^airlines/(?P<pk>[0-9]+)/$', view_airlines, name="view-airlines"),

    # Option to delete airlines, /flights/airlines/5/delete
    url(r'^airlines/(?P<pk>[0-9]+)/delete/$', delete_airlines, name="delete-airlines"),

    # Option to edit crew details, /flights/airlines/5/edit
    url(r'^airlines/(?P<pk>[0-9]+)/edit/$', edit_airlines, name="edit-airlines"),

]