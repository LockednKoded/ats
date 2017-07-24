from django.conf.urls import  url
from.import views

app_name='book'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^create/$',views.post_create,name='register'),
    url(r'^show/$',views.post_details,name='listbookings'),
]
