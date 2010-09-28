from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from django.views.generic.list_detail import object_list, object_detail
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

from jobs import models
from jobs.forms import DeveloperForm, JobForm, PasswordForm

def index(request):
    return add_developer(request)

def handle_form(request, Form, template_name):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            object = form.save()
            return HttpResponseRedirect(object.get_absolute_url())
    if request.method == 'GET':
        form = Form()
    payload = {'form':form}
    return render_to_response(template_name, payload, RequestContext(request))

def add_developer(request):
    return handle_form(request, DeveloperForm, 'jobs/adddev.html')

def add_job(request):
    return handle_form(request, JobForm, 'jobs/addjob.html')

def developer(request, id):
    qs = models.Developer.objects.all()
    return object_detail(request, template_name = 'jobs/developer.html', queryset = qs, object_id = id, template_object_name = 'developer')
    

def job(request, id):
    qs = models.Job.objects.all()
    return object_detail(request, template_name = 'jobs/job.html', queryset = qs, object_id = id, template_object_name = 'job')

def developers(request):
    try:
        order_by = request.GET['order']
    except:
        order_by = 'created_on'
    if order_by == 'created_on': order_by = '-created_on'
    if not order_by in ('name', 'created_on'):
        order_by = '-created_on'        
    qs = models.Developer.objects.all().order_by(order_by)
    return object_list(request, template_name = 'jobs/developers.html', queryset = qs, template_object_name = 'developers', paginate_by=10)

def jobs(request):
    try:
        order_by = request.GET['order']
    except:
        order_by = 'created_on'
    if order_by == 'created_on': order_by = '-created_on'
    if not order_by in ('name', 'created_on'):
        order_by = '-created_on'
    qs = models.Job.objects.all().order_by(order_by)
    return object_list(request, template_name = 'jobs/jobs.html', queryset = qs, template_object_name = 'jobs', paginate_by=10)

def edit_job(request, id):
    try:
        job = models.Job.objects.get(id = id)
    except models.Job,DoesNotExist:
        raise Http404
    if not job.is_editable:
        raise Http404
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == job.password:
                request.session['job_edit_rights'] = id
                redir_url = reverse('jobs_edit_job_done', args=[id])
                return HttpResponseRedirect(redir_url)
            else:
                return HttpResponseForbidden('Wrong password. Go back and try again.')
    if request.method == 'GET':
        form = PasswordForm()
    payload = {'form':form}
    return render_to_response('jobs/editdev.html', payload, RequestContext(request))

def edit_developer(request, id):
    try:
        dev = models.Developer.objects.get(id = id)
    except models.Developer.DoesNotExist:
        raise Http404
    if not dev.is_editable:
        raise Http404    
    if request.method == 'POST':
        form = PasswordForm(request.POST)        
        if form.is_valid():
            if form.cleaned_data['password'] == dev.password:
                request.session['dev_edit_rights'] = id
                redir_url = reverse('jobs_edit_developer_done', args=[id])
                return HttpResponseRedirect(redir_url)
            else:
                return HttpResponseForbidden('Wrong password. Go back and try again.')
    if request.method == 'GET':
        form = PasswordForm()
    payload = {'form':form}
    return render_to_response('jobs/editdev.html', payload, RequestContext(request))

def edit_job_done(request, id):
    job = models.Job.objects.get(id = id)
    if not job.is_editable:
        raise Http404    
    if request.method == 'POST':
        form = JobForm(request.POST, instance = job)
        if form.is_valid():
            job = form.save()
            return HttpResponseRedirect(job.get_absolute_url())
    elif request.method == 'GET':
        job = models.Job.objects.get(id = id)
        form = JobForm(instance = job)
    payload = {'form': form}
    return render_to_response('jobs/editjob.html', payload, RequestContext(request))
    
def edit_developer_done(request, id):
    dev = models.Developer.objects.get(id = id)
    if not dev.is_editable:
        raise Http404    
    if request.method == 'POST':
        form = DeveloperForm(request.POST, instance = dev)
        if form.is_valid():
            dev = form.save()
            return HttpResponseRedirect(dev.get_absolute_url())
    elif request.method == 'GET':
        dev = models.Developer.objects.get(id = id)
        form = DeveloperForm(instance = dev)
    payload = {'form': form}
    return render_to_response('jobs/adddev.html', payload, RequestContext(request))
