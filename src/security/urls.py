from django.conf.urls import url
from .views import *

app_name = "security"

urlpatterns = [


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