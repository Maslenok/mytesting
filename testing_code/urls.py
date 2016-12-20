from django.conf.urls import url
from .models import Course
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.course),
    url(r'^(\d+_[A-Za-z]+)/testing/$', views.question),
    url(r'^(\d+_[A-Za-z]+)/$', views.tests),



    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:
   # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)