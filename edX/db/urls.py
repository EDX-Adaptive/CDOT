from django.conf.urls import patterns, url, include
from django.views.generic.base import TemplateView
from db import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^base', views.base, name='base'),
        url(r'^login', views.login_page, name='auth_login'),
        url(r'^logout', views.logout_page, name='auth_logout'),
        url(r'^profile', views.profile, name='accounts_overview'),
        url(r'^list', views.list, name='list_all'),
        url(r'^databases/$', views.DatabaseList.as_view(), name='database_list'),
        url(r'^databases/create', views.DatabaseCreate.as_view(), name='database_create'),
        url(r'^databases/update', views.DatabaseUpdate.as_view(), name='database_update'),
        url(r'^databases/delete', views.DatabaseDelete.as_view(), name='database_delete'),
        url(r'^(?P<slug>[-_\w]+)/$', views.DatabaseDetail.as_view(), name='database_detail'),
        url(r'^state', views.state)
)
