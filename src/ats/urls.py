

"""ats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^flights/', include('flight_info.urls')),
    url(r'^parking/', include('parking.urls')),
    url(r'^$', home_page, name='home_page'),
    url(r'^contact/', contact_us, name='contact_us'),
    url(r'^services/', services, name='services'),
    url(r'^staff/', staff, name='staff'),
    url(r'^about/', about_us, name='about_us'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)