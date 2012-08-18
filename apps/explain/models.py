from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):

    #created_date = models.DateTimeField(auto_add_now=True)
    #deleted_date = models.DateTimeField()
    #deleted = models.BooleanField(default=False)

class Entry(Base):
    """ Describes an Entry"""
    
    #hex
    #name
    #slug
    #type

    #created_date = models.DateTimeField(auto_add_now=True)
    #deleted_date = models.DateTimeField()
    #deleted = models.BooleanField(default=False)
    
    #original_creator

    #submitted num
        
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

