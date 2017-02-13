from app.testing.models import Course
from mytesting import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import ListView

from . import views

urlpatterns = [

                  url(r'^(\d+_.*)/testing/$', views.question),
                  url(r'^(\d+_.*)/$', views.tests),
                  url(r'^$', ListView.as_view(model=Course)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
