from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

from django.contrib import admin

from jobs.views import Developers, Jobs, Developer, Job

admin.autodiscover()

urlpatterns = patterns('jobs.views',
    # Example:
    url(r'^$', 'index', name='jobs_index'),
    url(r'^adddev/$', 'add_developer', name='jobs_add_developer'),
    url(r'^addjob/$', 'add_job', name='jobs_add_job'),
    url(r'^developers/$', Developers.as_view(), name='jobs_developers'),
    url(r'^jobs/$', Jobs.as_view(), name='jobs_jobs'),
    url(r'^job/(?P<pk>\d+)/$', Job.as_view(), name='jobs_job'),
    url(r'^editjob/(?P<id>\d+)/$', 'edit_job', name='jobs_edit_job'),
    url(r'^editjob/(?P<id>\d+)/done/$', 'edit_job_done', name='jobs_edit_job_done'),
    url(r'^developer/(?P<pk>\d+)/$', Developer.as_view(), name='jobs_developer'),
    url(r'^editdev/(?P<id>\d+)/$', 'edit_developer', name='jobs_edit_developer'),
    url(r'^editdev/(?P<id>\d+)/done/$', 'edit_developer_done', name='jobs_edit_developer_done'),
    url(r'^about/$', TemplateView.as_view(template_name='jobs/about.html'), name='jobs_about'),

    # Uncomment this for admin:
    # url(r'^admin/', include(admin.site.urls)),
)


