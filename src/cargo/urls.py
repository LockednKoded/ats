from django.conf.urls import url
from . import views
from .views import *

app_name = "cargo"

urlpatterns = [


    # Homepage for cargo, showing a list of all scheduled cargo, /cargo/
    url(r'^$' , views.index , name="index"),

    # Option to view cargo details, /cargo/5/
    url(r'^(?P<pk>[0-9]+)/$',views.view_cargo, name="view-cargo"),

    url(r'^disclaimer$' , views.disclaimer , name="disclaimer"),

    url(r'^procedure$', views.procedure, name="procedure"),

    url(r'^cargolist$', views.cargolist, name="cargolist"),

    url(r'^list$' , views.list_cargo, name="cargo_list"),

    url(r'^bookcargo$', views.bookcargo, name="cargo_book"),

    # Option to delete cargo, /flights/5/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', delete_cargo, name="delete-cargo"),

    # Option to edit cargo details, /cargo/5/edit
    url(r'^edit/(?P<pk>[0-9]+)/$', edit_cargo, name="edit-cargo"),

    url(r'^faq$', views.faq, name="faq"),

    url(r'^faretable$', views.faretable, name="fare-table"),


    url(r'^guideline$', views.guideline, name="guideline"),

    url(r'^export$', views.export, name="export"),

    url(r'^aboutus$', views.aboutus, name="aboutus"),

    url(r'^helpandsupport$', views.helpandsupport, name="helpandsupport"),

# Option to add new cargo, /cargo/add/
    url(r'^add/$', add_cargo, name="add-cargo"),

    # Option to delete cargo, /cargo/5/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$', delete_cargo, name="delete-cargo"),
]

