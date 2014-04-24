"""Map URL requests to their respective functions or files."""
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from homepage import views


urlpatterns = \
    patterns('',
             url(r'^$', views.index, name='index'),
             url(r'^screenshots/$', views.screenshots, name='screenshots'),
             url(r'^license/$', views.license, name='license'),
             url(r'^contributing/$', views.contribute, name='contribute'),
             url(r'^download/$',
                 TemplateView.as_view(template_name='download.html'),
                 name='download'),
             url(r'^community/$',
                 TemplateView.as_view(template_name='community.html'),
                 name='community'),
             )
