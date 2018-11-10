from django.conf.urls import url, include
from . import views



urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$', views.new),
    url(r'^display$', views.index),
    url(r'^test/$', views.test),
    url(r'^create/$', views.index),
    url(r'^(?P<show_number>\d+)/$', views.show),
    url(r'^(?P<show_number>\d+)/edit/$', views.edit),
    url(r'^(?P<show_number>\d+)/delete/$', views.destroy),

]  
