from tastypie.resources import ModelResource
from explain.models import Entry, Comment
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


class CommentAPIResource(ModelResource):
    """
    API for comments
    """

    class Meta:
        queryset = Comment.objects.all()
        resource = "comment"
        allowed_methods = ['get']
