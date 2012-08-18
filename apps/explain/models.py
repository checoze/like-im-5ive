from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    """ Describes an Entry"""
    #name
    #slug
    #type

    #created_date = models.DateTimeField(auto_add_now=True)
    #deleted_date = models.DateTimeField()
    #deleted = models.BooleanField(default=False)
    
    #original_creator

    #submitted
        
    def __unicode__(self):
        return str(self.slug)

