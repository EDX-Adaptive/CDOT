from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('db.urls')),
    url(r'^db/', include('db.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
