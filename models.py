from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    email = models.EmailField()
    website = models.URLField(null = True)
    location = models.CharField(null = True, max_length = 100)
    created_on = models.DateTimeField(auto_now_add = 1)
    #Edit info
    is_editable = models.BooleanField(default = False)
    password = models.CharField(max_length = 100, null = True)
    
    @models.permalink
    def get_absolute_url(self):
        return ('jobs.views.developer', [self.id])
    
    @models.permalink
    def get_edit_url(self):
        return ('jobs.views.edit_developer', [self.id])
        
    class Admin:
        pass
    
    class Meta:
        ordering = ('-created_on', )
    
class Job(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    budget = models.PositiveIntegerField(null = True)
    on_site = models.BooleanField(default = False)
    location = models.CharField(max_length = 100, null = True)
    created_on = models.DateTimeField(auto_now_add = 1)
    #Posters Info
    poster_name = models.CharField(max_length = 100)
    email = models.EmailField()
    website = models.URLField(null = True)
    other_info = models.CharField(max_length = 100, null = True)
    #Edit info
    is_editable = models.BooleanField(default = False)
    password = models.CharField(max_length = 100, null = True)
    
    @models.permalink
    def get_absolute_url(self):
        return ('jobs.views.job', [self.id])
    
    @models.permalink
    def get_edit_url(self):
        return ('jobs.views.edit_job', [self.id])

    class Admin:
        pass
    
    class Meta:
        ordering = ('-created_on', )