from django.conf.urls import url
from .models import Course

from . import views

urlpatterns = [
    
   
    #url(r'^S', views.detail),
    url(r'^', views.index, name='index'),
    
]