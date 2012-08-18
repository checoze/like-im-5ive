from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    """ Base model that contains creation data """

    created_date = models.DateTimeField(auto_add_now=True)
    deleted_date = models.DateTimeField()
    deleted = models.BooleanField(default=False)

class Entry(Base):
    """ Describes an Entry"""
    
    #hex
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    type  = models.CharField(max_length=40)
    
    original_creator = model.ForeignKey(Entry)
        
    def __unicode__(self):
        return str(self.slug)
        
class Explanation(Base):
    """ An Explanation that points to an Entry """
    
    entry = model.ForeignKey(Entry)
    body = models.TextField()

    #upvotes
    #downvotes
    #submitted
        
    def __unicode__(self):
        return str(self.body)


class Comment(Base):
    """ Comments on an Explanation. """
    
    user = model.ForeignKey(User)
    body = models.TextField()
    
    def __unicode__(self):
        return str(self.body)