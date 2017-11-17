# howdy/urls.py
from django.conf.urls import url
from .views import api
from .views import auth

urlpatterns = [
    url(r'^shorten/$', api.shorten),
    url(r'^r/(?P<token>\.{0,32})/$', api.r),
    url(r'^authenticate/$', api.r),
]