from django.conf.urls import url
from .models import Course
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    
   
    #url(r'^S', views.detail),
    url(r'^', views.index, name='index'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:
   # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)