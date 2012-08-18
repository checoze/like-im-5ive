from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('explain.urls')),
    url(r'^accounts/login/$', "django.contrib.auth.views.login", {'template_name': "explain/home.html"}, name="login"),
    url(r'^accounts/logout/$', "django.contrib.auth.views.logout", {'template_name': "explain/home.html"}, name="logout"),
    url(r'^accounts/registration/$', "explain.views.registration", name="registration"),
    url(r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    import os

    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
        url(r'^help/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.SITE_ROOT, "docs/build/html") }),
    )
    urlpatterns += staticfiles_urlpatterns()

