from django.conf.urls import url
from .views import *

app_name = "security"

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

    # Option to edit flight details, /flights/5/edit                    #done view
    url(r'^(?P<pk>[0-9]+)/edit/$', edit_flight, name="edit-flight"),




    # Force_employee Options:

    # Option to view all crew/pilots, /flights/crew
    url(r'^force_employee/$', list_force_employee, name="list-force_employee"),

    # Option to add crew, /flights/crew/add
    url(r'^force_employee/add/$', add_force_employee, name="add-force_employee"),

    # Option to view crew details, /flights/crew/5
    url(r'^force_employee/(?P<pk>[0-9]+)/$', view_force_employee, name="view-force_employee"),

    # Option to delete crew, /flights/crew/5/delete
    url(r'^force_employee/(?P<pk>[0-9]+)/delete/$', delete_force_employee, name="delete-force_employee"),

    # Option to edit crew details, /flights/crew/5/edit
    url(r'^force_employee/(?P<pk>[0-9]+)/edit/$', edit_force_employee, name="edit-force_employee"),



]

#security_forces

# Option to view all crew/pilots, /flights/crew
url(r'^security_forces()/$', list_security_forces(), name="list-security_forces()"),

# Option to add crew, /flights/crew/add
url(r'^security_forces()/add/$', add_security_forces(), name="add-security_forces()"),

# Option to view crew details, /flights/crew/5
url(r'^security_forces()/(?P<pk>[0-9]+)/$', view_security_forces(), name="view-security_forces()"),

# Option to delete crew, /flights/crew/5/delete
url(r'^security_forces()/(?P<pk>[0-9]+)/delete/$', delete_security_forces(), name="delete-security_forces()"),

# Option to edit crew details, /flights/crew/5/edit
url(r'^security_forces()/(?P<pk>[0-9]+)/edit/$', edit_security_forces(), name="edit-security_forces()"),