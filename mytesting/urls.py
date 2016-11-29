"""mytesting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,  include
from django.contrib import admin
#import testing_code
from testing_code.views import index, course
from result.views import result
from django.conf import settings
from django.conf.urls.static import static
#from testing_code.models import Course

urlpatterns = [
     url(r'^admin/', admin.site.urls),
     # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
     url(r'^course/$', course),
     url(r'^course/', include("testing_code.urls")),
     url(r'^statistics/$', result),
     url(r'^', index),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
  #  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
