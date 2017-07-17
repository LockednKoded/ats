from django.conf.urls import url

from .views import (login_view, logout_view, register_view, profile_edit_view, profile_detail_view)

app_name = "accounts"

urlpatterns = [

    # /accounts/login/
    url(r'^login/$', login_view, name="login"),

    # /accounts/logout/
    url(r'^logout/$', logout_view, name="logout"),

    # /accounts/register/
    url(r'register/$', register_view, name="register"),

    # /accounts/7/profile
    url(r'^(?P<pk>[0-9]+)/profile/$', profile_detail_view, name="view-profile"),

    # /accounts/7/profile/edit
    url(r'^(?P<pk>[0-9]+)/profile/edit/$', profile_edit_view, name="edit-profile"),
]