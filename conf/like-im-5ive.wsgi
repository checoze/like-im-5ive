import os, sys, site


# Fix markdown.py (and potentially others) using stdout
sys.stdout = sys.stderr

#Root of Project is up one directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))


#add virtual env path
#site.addsitedir('/srv/www/.virtualenvs/PROJECT/lib/python2.6/site-packages/')

#prod or alpha
from conf.environment import PROJECT_ENV
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.%s' % PROJECT_ENV

rom django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
application = newrelic.agent.wsgi_application()(application)

