from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^list/', 'riverview.views.list'),
    (r'^$','riverview.views.index'),

    (r'^view/', include('riverview.urls')),
    (r'^page/', include('page.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
   
 #    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/data/projects/river-studies/django/apps/riverstudies/media'}),

)

