import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages

setup(
    name="django-jobs",
    version="0.1",
    packages=['django-jobs'],
    package_data={'django-jobs': ['templates/*.html', 
                                 'templates/jobs/*.html'],
                 },
    zip_safe=False,
    author="Agiliq Solutions",
    author_email="hello@agiliq.com",
    description="A job board for Python",
    url="http://agiliq.com/",
)
