from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects/', views.projects, name='projects'),
    url(r'^projectservices/(?P<pk>[0-9]+)/', views.projectservices, name='projectservices'),
    url(r'^projectcar/(?P<pk>[0-9]+)/', views.projectcar, name='projectcar'),
    url(r'^project/(?P<pk>[0-9]+)/', views.project, name='project'),
    url(r'^services/', views.services, name='services'),
    url(r'^news/', views.news, name='news'),
    ]
