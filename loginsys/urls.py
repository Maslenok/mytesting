from django.conf.urls import url

import loginsys
from loginsys.views import logout, login
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^logout/$', logout),
    url(r'^login/$', login),
    #url(r'^register/$', register),
    url(r'^register/$', loginsys.views.RegisterFormView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:
   # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)