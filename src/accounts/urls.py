from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .views import *

app_name = "accounts"

urlpatterns = [

    # /accounts/login/
    url(r'^login/$', CustomLoginView.as_view(), name="login"),

    # /accounts/logout/
    url(r'^logout/$', auth_views.LogoutView.as_view(), name="logout"),

]