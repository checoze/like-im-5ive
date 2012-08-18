import random
from explain.managers import VoteManager
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Base(models.Model):
    """ Base model that contains creation data """

    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    
    class Meta:
        abstract = True
    
class EntryManager(models.Manager):
    def get_until_create(self):
        created = False
        while not created:
            hex = ''.join(random.choice('0123456789abcdef') for i in range(6))
            entry, created = Entry.objects.get_or_create(hex=hex)
            if created:
                return entry

class Entry(Base):
    """ Describes an Entry"""
    
    objects = EntryManager()
    
    hex = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    type  = models.CharField(max_length=40)
    
    original_creator = models.ForeignKey(User, default="1")
        
    def __unicode__(self):
        return str("%s - %s" % (self.hex, self.name))
    
    def save(self, *args, **kwargs):
        if not self.hex:
            _hex = ''.join(random.choice('0123456789abcdef') for i in range(6))
            self.hex = _hex
        
        self.slug = slugify(self.name)
            
        super(Entry, self).save(*args, **kwargs)
    
    def get_most_popular_explanation(self):
        return self.explanation_set.all().get(id=2)

        
class Explanation(Base):
    """ An Explanation that points to an Entry """

    objects = EntryManager()
    
    entry = models.ForeignKey(Entry)
    body = models.TextField()

    #submitted #
        
    def __unicode__(self):
        return str(self.body)


class Comment(Base):
    """ Comments on an Explanation. """
    
    user = models.ForeignKey(User)
    body = models.TextField()
    
    def __unicode__(self):
        return str(self.body)
        
        
class Vote(Base):
    """ Keep track of votes for objects on the site. """

    user = models.ForeignKey(User)
    value = models.BooleanField(default=False)
    
    # Content-object field
    content_type = models.ForeignKey(ContentType,
            verbose_name=('content type'),
            related_name="content_type_set_for_%(class)s")
    object_pk = models.TextField(('object ID'))
    content_object = generic.GenericForeignKey(ct_field="content_type", fk_field="object_pk")

    objects = VoteManager()