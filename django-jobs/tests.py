"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse



class JobsAppTestcase(TestCase):

    def setUp(self):
        self.c = Client()

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

        