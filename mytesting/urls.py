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

from django.conf import settings
from django.conf.urls import url,  include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import DetailView

from app.testing.models import AboutPage
from mytesting import settings
from app.result.views import result
from app.testing.views import  AboutPageList

urlpatterns = [
     url(r'^admin/', admin.site.urls),
     url(r'^course/', include("app.testing.urls")),
     url(r'^statistics/', result),     
     url(r'^auth/', include("core.urls")),
     #url(r'^profile/', index1),.
     #url (r'^ckeditor/', include('ckeditor.urls')),
     url(r'^nested_admin/', include('nested_admin.urls')),
     url(r'^', AboutPageList.as_view(), name='list'),
    # url(r'^', index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



