from django import forms

from jobs import models

class DeveloperForm(forms.ModelForm):
    name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'size':50, 'class':"text"}), help_text="Your or Company's name. This field is required.")
    description = forms.CharField(widget = forms.Textarea({'class':"text"}), help_text = 'Some description about you, links to sample work, testimonials etc. This field is required.')
    email = forms.EmailField(widget = forms.TextInput(attrs={'size':50, 'class':"text"}), help_text='Your email. This field is required.')
    website = forms.URLField(required = False, widget = forms.TextInput(attrs={'size':50, 'class':"text"}), help_text='Link to your website.')
    location = forms.CharField(required = False, max_length = 100, widget = forms.TextInput(attrs={'size':50, 'class':"text"}), help_text='Where are you located?')
    #Edit info
    password = forms.CharField(max_length = 100, required = False,  widget = forms.PasswordInput(attrs={'size':50, 'class':"text"}), help_text='Enter a password, if you would like to edit this in future. This password is saved in cleartext, so do not use a valuable password.')
    
    class Meta:
        model = models.Developer
        exclude = ('is_editable')
        
    def save(self):
        developer = super(DeveloperForm, self).save()
        if developer.password:
            developer.is_editable = True
            developer.save()
        return developer
        
class JobForm(forms.ModelForm):
    name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'size':50}), label='Job Name', help_text = 'Name of the job/contract')
    description = forms.CharField(max_length = 100, widget = forms.Textarea, help_text = 'Some information about the job/contract.')
    budget = forms.IntegerField(widget = forms.TextInput(attrs={'size':50}), required=False, help_text = 'Budget/Salary for this contract/job.')
    on_site = forms.BooleanField(widget = forms.TextInput(attrs={'size':50}),required=False, help_text = 'Are peole required to be on site?')
    location = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'size':50}), required=False, help_text= 'Where is this located?')
    #Posters Info
    poster_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'size':50}), help_text = "Your /Your company's name.", label='Your Name')
    email = forms.EmailField(widget = forms.TextInput(attrs={'size':50}),help_text = 'Your email id.')
    website = forms.URLField(widget = forms.TextInput(attrs={'size':50}), required=False, help_text = 'Your website.')
    other_info = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'size':50}), required=False, help_text = 'Some information about you.')
    #Edit info
    password = forms.CharField(max_length = 100, required = False, widget = forms.PasswordInput(attrs={'size':50}), help_text = 'If you want this job to be editable, enter a password. This password is saved in cleartext, so do not use a valuable password.')
    
    class Meta:
        model = models.Job
        exclude = ('is_editable')
        
    def save(self):
        job = super(JobForm, self).save()
        if job.password:
            job.is_editable = True
            job.save()
        job.save()
        return job
        
class PasswordForm(forms.Form):
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'size':50}), help_text = 'Enter the passwords assocoiated with this posting.')
