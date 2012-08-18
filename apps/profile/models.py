from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """ Extended information stored about the user """
    user = models.ForeignKey(User, unique=True)
    
    bio = models.TextField(blank=True)
    
    #Entries submitted
    #submited
    #comments
    
    def __unicode__(self):
        return str(self.user)
        

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
