from settings.common import *

MEDIA_ROOT = '/home/user/projects/project/media/'
MEDIA_URL = '/media/'

STATIC_ROOT = '/srv/www/static/%s' % PROJECT_ID
STATIC_URL = '/static/%s/' % PROJECT_ID


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


