from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('jobs.views',
    # Example:
    url(r'^$', 'index', name='jobs_index'),
    url(r'^adddev/$', 'add_developer', name='jobs_add_developer'),
    url(r'^addjob/$', 'add_job', name='jobs_add_job'),
    url(r'^developers/$', 'developers', name='jobs_developers'),
    url(r'^jobs/$', 'jobs', name='jobs_jobs'),
    url(r'^job/(?P<id>\d+)/$', 'job', name='jobs_job'),
    url(r'^editjob/(?P<id>\d+)/$', 'edit_job', name='jobs_edit_job'),
    url(r'^editjob/(?P<id>\d+)/done/$', 'edit_job_done', name='jobs_edit_job_done'),
    url(r'^developer/(?P<id>\d+)/$', 'developer', name='jobs_developer'),
    url(r'^editdev/(?P<id>\d+)/$', 'edit_developer', name='jobs_edit_developer'),
    url(r'^editdev/(?P<id>\d+)/done/$', 'edit_developer_done', name='jobs_edit_developer_done'),
    url(r'^about/$', direct_to_template, {'template':'jobs/about.html'}, name='jobs_about'),

    # Uncomment this for admin:
    ('^admin/(.*)', admin.site.root),
)


