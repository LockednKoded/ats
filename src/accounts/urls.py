from django.conf.urls import url

from .views import (CustomLogoutView,
                    CustomLoginView,
                    RegisterView, )

app_name = "accounts"

urlpatterns = [

    # /accounts/login/
    url(r'^login/$', CustomLoginView.as_view(), name="login"),

    # /accounts/logout/
    url(r'^logout/$', CustomLogoutView.as_view(), name="logout"),

    # /accounts/register/
    # url(r'register/$', register_view, name="register"),
    url(r'register/$', RegisterView.as_view(), name="register"),

]