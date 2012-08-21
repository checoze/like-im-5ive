from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api
from explain.api import EntryResource

v1_api = Api(api_name="v1")
v1_api.register(EntryResource())

urlpatterns = patterns('',

    url(r'^$', 'explain.views.home', name='home'),

    url(r'^search$', 'explain.views.search', name='search'),
    url(r'^entry/create', 'explain.views.entry_create', name='entry_create'),
    url(r'^([a-f0-9]{6})/', 'explain.views.entry_detail', name='entry_detail'),
    
    url(r'^explanation/submit$', 'explain.views.explanation_submit', name='explanation_submit'),
    
    #Voting
    url(r'^vote/explanation/(\d+)/$', 'explain.views.vote', {'type':'explanation'}, name='vote_explanation'),
    url(r'^vote/comment/(\d+)/$', 'explain.views.vote', {'type':'comment'}, name='vote_comment', ),

    # API
    url(r'api/', include(v1_api.urls)),
)
