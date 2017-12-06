from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^projects/(?P<pk>[0-9]+)/', views.projectsmodel, name='projectsmodel'),
    url(r'^projects/', views.projects, name='projects'),

    url(r'^photogallery/(?P<pk>[0-9]+)/', views.photogallery, name='photogallery'),
    url(r'^project/(?P<pk>[0-9]+)/', views.project, name='project'),

    url(r'^service/(?P<pk>[0-9]+)/', views.service, name='service'),
    url(r'^services/(?P<pk>[0-9]+)/', views.services, name='services'),

    url(r'^news/(?P<pk>[0-9]+)/', views.newsmodel, name='newsmodel'),
    url(r'^news/', views.news, name='news'),

    url(r'^gallery/(?P<pk>[0-9]+)/', views.galleryserv, name='galleryserv'),
    url(r'^gallery/', views.gallery, name='gallery'),

    url(r'^article/(?P<pk>[0-9]+)/', views.article, name='article'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^vacancy/', views.vacancy, name='vacancy'),
    url(r'^about/', views.about, name='about'),

    url(r'^model/(?P<pk>[0-9]+)/', views.model, name='model'),
    
    url(r'^askme/', views.askme, name='askme'),
    ]
