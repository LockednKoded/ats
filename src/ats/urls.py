
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    
    url(r'^cargo/',include('cargo.urls')),
    url(r'^flights/', include('flight_info.urls')),
    url(r'^parking/', include('parking.urls')),
    url(r'^baggage_handling/', include('baggage_handling.urls')),
    url(r'^maintenance/', include('maintenance.urls')),
    url(r'^book/', include('book.urls')),  
    
    url(r'^$', homepage, name='homepage'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)