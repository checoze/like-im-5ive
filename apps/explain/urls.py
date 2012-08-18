from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api
from explain.api import EntryResource, CommentAPIResource

v1_api = Api(api_name="v1")
v1_api.register(EntryResource())
v1_api.register(CommentAPIResource())

urlpatterns = patterns('',

    url(r'^$', 'explain.views.home', name='home'),

    url(r'^entry/create$', 'explain.views.entry_prompt', name='entry_prompt'),
    url(r'^entry/submit$', 'explain.views.entry_submit', name='entry_submit'),
    url(r'^([a-f0-9]{6})/', 'explain.views.entry_detail', name='entry_detail'),
    
    url(r'api/', include(v1_api.urls)),
)
