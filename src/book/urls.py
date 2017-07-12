from django.conf.urls import  url
from.import views


urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^create/$',views.post_create,name='oja'),
url(r'^show/$',views.post_details,name='gar'),
]
