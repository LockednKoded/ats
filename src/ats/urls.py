from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import *

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

    url(r'^contact/', contact_us, name='contact_us'),
    url(r'^services/', services, name='services'),
    url(r'^developedby/', developedby, name='developedby'),
    url(r'^about/', about_us, name='about_us'),

    
    url(r'^$', home_page, name='home_page'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
