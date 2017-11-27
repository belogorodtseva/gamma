from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects/', views.projects, name='projects'),
#    url(r'^gallery/', views.gallery, name='gallery'),
#    url(r'^photogallery/(?P<pk>[0-9]+)/', views.photogallery, name='photogallery'),
#    url(r'^project/(?P<pk>[0-9]+)/', views.project, name='project'),
#    url(r'^services/', views.services, name='services'),
#    url(r'^service/(?P<pk>[0-9]+)/', views.service, name='service'),
    url(r'^news/', views.news, name='news'),
    url(r'^galleries/', views.gallerys, name='gallerys'),
#    url(r'^news/(?P<pk>[0-9]+)/', views.newsuno, name='newsuno'),
#    url(r'^contact/', views.contact, name='contact'),
    ]
