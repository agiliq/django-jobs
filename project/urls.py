from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    url(r'^', include('jobs.urls')),
)

# if settings.DEBUG:
#     urlpatterns += patterns('django.views.static',
#         (r'^site_media/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}),
#     )


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)