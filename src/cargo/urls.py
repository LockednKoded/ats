from django.conf.urls import url
from . import views

app_name = "cargo"

urlpatterns = [

    # Cargo Options:

    # Homepage for cargo, showing a list of all scheduled cargo, /cargo/
    url(r'^$' , views.index , name="index"),

    # Option to view cargo details, /cargo/5/
    url(r'^(?P<pk>[0-9]+)/$',views.view_cargo, name="view-cargo"),

]

