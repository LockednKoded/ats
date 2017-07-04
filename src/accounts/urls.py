from django.conf.urls import url

from .views import (login_view, logout_view, register_view,)

app_name = "accounts"

urlpatterns = [

    # /accounts/login/
    url(r'^login/$', login_view, name="login"),

    # /accounts/logout/
    url(r'^logout/$', logout_view, name="logout"),

    # /accounts/register/
    url(r'register/$', register_view, name="register"),

]