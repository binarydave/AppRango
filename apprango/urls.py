__author__ = 'gray'

from django.conf.urls import patterns, url
from apprango import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^category/(?P<slug_item>[\w\-]+)/$', views.category, name='category'),
                       url(r'^add-category/$', views.add_category, name='add-category'),
                       url(r'^(?P<slug_item>[\w\-]+)/add-page/$', views.add_page, name='add-page'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.login, name='login'),
                       url(r'^restricted/$', views.restricted, name='restricted'),
                       url(r'^logout/$', views.logout, name='logout'))