"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# import newrelic.agent
# newrelic.agent.initialize(os.path.join(os.path.dirname(__file__), "newrelic.ini"))
import newrelic.agent
newrelic.agent.initialize('newrelic.ini')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

application = get_wsgi_application()
