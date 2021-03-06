from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.static import serve

# admin.autodiscover()
import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tasting.views.home', name='home'),
    # url(r'^tasting/', include('tasting.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment 
    (r'^resources/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
                
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                              
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('core.urls')),
)
