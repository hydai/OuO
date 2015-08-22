from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^create/(?P<tid>\d+)$', views.create, name='create'),
    url(r'^result/(?P<gid>\d+)$', views.result, name='result'),
)
