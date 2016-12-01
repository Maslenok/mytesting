from django.conf.urls import url
from loginsys.views import logout, login, register
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^logout/$', logout),
    url(r'^login/$', login),
    url(r'^register/$', register),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:
   # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)