from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^create/(?P<tid>\d+)$', views.create, name='create'),
    url(r'^json/(?P<gid>\d+)$', views.mapping_json, name='mapping_json'),
    url(r'^result/(?P<gid>\d+)$', views.result, name='result'),
)
