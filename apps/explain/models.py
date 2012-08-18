import random

from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    """ Base model that contains creation data """

    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)


class Entry(Base):
    """ Describes an Entry"""
    
    #objects = EntryManager()
    
    hex = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    type  = models.CharField(max_length=40)
    
    original_creator = models.ForeignKey(User)
        
    def __unicode__(self):
        return str(self.slug)
    
    def save(self, *args, **kwargs):
        if not self.hex:
            _hex = ''.join(random.choice('0123456789abcdef') for i in range(6))
            self.hex = _hex
        super(Entry, self).save(*args, **kwargs)
        
class Explanation(Base):
    """ An Explanation that points to an Entry """
    
    entry = models.ForeignKey(Entry)
    body = models.TextField()

    #upvotes
    #downvotes
    #submitted
        
    def __unicode__(self):
        return str(self.body)


class Comment(Base):
    """ Comments on an Explanation. """
    
    user = models.ForeignKey(User)
    body = models.TextField()
    
    def __unicode__(self):
        return str(self.body)