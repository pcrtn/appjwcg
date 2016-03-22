from django.conf.urls import patterns, url
from contactos import views

urlpatterns = patterns('',
  url(r'^$', views.co_list, name='co_list'),
  url(r'^new$', views.co_add, name='co_add'),
  url(r'^view/(?P<pk>\d+)$', views.co_view, name='co_view'),
  url(r'^edit/(?P<pk>\d+)$', views.co_edit, name='co_edit'),
  #url(r'^delete/(?P<pk>\d+)$', views.server_delete, name='server_delete'),
)