from django.conf.urls import url
from django.views.generic import TemplateView
from core.views import UserUpdateView,get_robots_txt, landing_login,landing_registration,login,logout,RegisterFormView




urlpatterns = (

    url(r'^robots\.txt', (get_robots_txt), name='robots'),
    url(r'^profile/$', UserUpdateView.as_view(), name='profile'),
    url(r'^accounts/login/$', (landing_login), name='login'),
    url(r'^accounts/registration/$', (landing_registration), name='registration'),
    url(r'^logout/$', logout),
    url(r'^login/$', login),
    url(r'^register/$', RegisterFormView.as_view()),
)