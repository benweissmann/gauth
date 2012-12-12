from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('redirector.views',
    url(r'^forms/(?P<form_key>[0-9a-f]+)$', 'redirect'),
    url(r'^tokens/(?P<token>[0-9a-f]+)$', 'resolve'),
    url(r'^$', 'index')

)

urlpatterns += patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)