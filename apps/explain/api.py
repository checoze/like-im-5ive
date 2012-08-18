from tastypie.resources import ModelResource
from explain.models import Entry
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import ReadOnlyAuthorization

class EntryResource(ModelResource):
    """
    API for Entries
    """

    class Meta:
        queryset = Entry.objects.all()
        resource = "entry"
        allowed_methods = ['get']
