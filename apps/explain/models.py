import random
import urllib
from bs4 import BeautifulSoup

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from explain.managers import VoteManager, EntryManager

TAG_CHOICES= (
    ('sfw', 'Safe For Work'),
    ('nsfw', 'Not Safe For Work')
)

class Base(models.Model):
    """ Base model that contains creation data """

    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    
    class Meta:
        abstract = True
        
class Tag(models.Model):
    """ Tags for Entry types with URL  """

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=12, choices=TAG_CHOICES)
    
    def __unicode__(self):
        return str(self.name)
    
class Entry(Base):
    """ Describes an Entry"""
    
    objects = EntryManager()
    
    hex = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    
    #URL specific fields
    url = models.URLField(max_length=255, blank=True)
    
    original_creator = models.ForeignKey(User, default="1")
        
    def __unicode__(self):
        return str("%s - %s" % (self.hex, self.name))
    
    def save(self, *args, **kwargs):
        if not self.hex:
            _hex = ''.join(random.choice('0123456789abcdef') for i in range(6))
            self.hex = _hex
        
        
        if self.name.startswith('http' or 'www'):
            try:
            	url_data = urllib.urlopen(self.name)
            	url_html = url_data.read()

                try:
                    soup = BeautifulSoup(url_html)
                    self.url = self.name
                    self.name = soup.title.string
                except:
                    pass
            except Exception, e:
                print e
                pass
        
        self.slug = slugify(self.name)
            
        super(Entry, self).save(*args, **kwargs)
    
    def get_most_popular_explanation(self):
        explanation = sorted(self.explanation_set.all(), key=lambda a: a.score, reverse=True)[:1]
        return explanation
        
    def possibly_link(self):
        if self.name.startswith('http' or 'www'):
            return True
        else:
            return False
                
class Explanation(Base):
    """ An Explanation that points to an Entry """

    objects = EntryManager()
    
    entry = models.ForeignKey(Entry)
    body = models.TextField()


    tags = models.ManyToManyField(Tag, blank=True)
    #submitted #
        
    def __unicode__(self):
        return str(self.body)

    @property        
    def up_votes(self):
        up_votes = Vote.objects.for_model(self).get_up_votes().count()
        #print up_votes
        return int(up_votes)
        
    @property        
    def down_votes(self):
        down_votes = Vote.objects.for_model(self).get_down_votes().count()
        return int(down_votes)
        
    @property        
    def score(self):
        return int(self.up_votes - self.down_votes)




class Comment(Base):
    """ Comments on an Explanation. """
    
    user = models.ForeignKey(User)
    body = models.TextField()
    
    @property        
    def up_votes(self):
        up_votes = Vote.objects.for_model(self).get_up_votes().count()
        print up_votes
        return up_votes
        
    @property        
    def down_votes(self):
        down_votes = Vote.objects.for_model(self).get_down_votes().count()
        print down_votes
        return down_votes
    
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
