from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api
from explain.api import EntryResource

v1_api = Api(api_name="v1")
v1_api.register(EntryResource())
urlpatterns = patterns('',

    url(r'^$', 'explain.views.home', name='home'),
    url(r'api/', include(v1_api.urls)),
)
