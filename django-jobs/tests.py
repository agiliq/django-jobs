"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from jobs.models import Job, Developer
# from jobs.forms import DeveloperForm, JobForm, PasswordForm


class JobsAppTestcase(TestCase):

    def setUp(self):
        self.c = Client()
        # self.dev_form = DeveloperForm(name="Developer", description="Adding a Developer", email="admin@admin.com")
        # self.job_form = JobForm(name="Job", description="Adding a Job", poster_name="some comapny", email="admin@admin.com")
        # self.pas_form = PasswordForm(password="adminadmin")
        self.dev_form_data = {'name':"Developer", 'description':"Adding a Developer", 'email':"admin@admin.com"}
        self.job_form_data = {'name':'Job', "description":"Adding a Job", 'poster_name':"some company", 'email':"admin@admin.com"}

        self.pas_form = {'password':"adminadmin"}
        self.site = Site(domain='localhost:8000', name='localhost')

    def test_IndexView(self):
    	response = self.c.get(reverse("jobs_index"))
    	self.assertEqual(200, response.status_code)    

    def test_adddevview(self):
        response = self.c.get(reverse("jobs_add_developer"))
        self.assertEqual(200, response.status_code)

    def test_addjobview(self):
    	response = self.c.get(reverse("jobs_add_job"))
    	self.assertEqual(200, response.status_code)

    def test_developersview(self):
        response = self.c.get(reverse("jobs_developers"))
        self.assertEqual(200, response.status_code)

    def test_jobsview(self):
        response = self.c.get(reverse("jobs_jobs"))
        self.assertEqual(200, response.status_code)    

    def test_aboutview(self):
    	response = self.c.get(reverse("jobs_about"))
    	self.assertEqual(200, response.status_code)

    def test_addajobview(self):
        response = self.c.post(reverse('jobs_add_job'),self.job_form_data)
        self.assertEqual(302, response.status_code)

    def test_jobdetailview(self):
        response = self.c.post(reverse('jobs_add_job'),self.job_form_data, follow=True)
        response_present = self.c.get(response.redirect_chain[0][0])
        self.assertEqual(200, response_present.status_code)

    def test_addadevview(self):
        response = self.c.post(reverse('jobs_add_developer'),self.dev_form_data)
        self.assertEqual(302, response.status_code)

    def test_devdetailview(self):
        response = self.c.post(reverse('jobs_add_developer'),self.dev_form_data, follow=True)
        response_present = self.c.get(response.redirect_chain[0][0])
        self.assertEqual(200, response_present.status_code)

    def test_jobeditview(self):
        self.c.post(reverse('jobs_add_job'),self.job_form_data, follow=True)
        id = Job.objects.get(id=1)
        id.is_editable = True
        id.save()
        response = self.c.get(reverse('jobs_edit_job', kwargs={'id':id.id}))
        self.assertEqual(200, response.status_code)

    def test_jobeditdoneview(self):
        self.c.post(reverse('jobs_add_job'),self.job_form_data, follow=True)
        id = Job.objects.get(id=1)
        id.is_editable = True
        id.save()        
        response = self.c.get(reverse('jobs_edit_job_done', kwargs={'id':id.id}))
        self.assertEqual(200, response.status_code)        

    def test_deveditdview(self):
        self.c.post(reverse('jobs_add_developer'),self.dev_form_data, follow=True)
        id = Developer.objects.get(id=1)
        id.is_editable = True
        id.save()        
        response = self.c.get(reverse('jobs_edit_developer', kwargs={'id':id.id}))
        self.assertEqual(200, response.status_code)

    def test_deveditddoneview(self):
        self.c.post(reverse('jobs_add_developer'),self.dev_form_data, follow=True)
        id = Developer.objects.get(id=1)
        id.is_editable = True
        id.save()        
        response = self.c.get(reverse('jobs_edit_developer_done', kwargs={'id':id.id}))
        self.assertEqual(200, response.status_code)
