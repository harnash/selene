import re

from .base import *


DEBUG = False

# Send emails to the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# or, use GMail
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'USERNAME@gmail.com'
#EMAIL_HOST_PASSWORD = 'PASSWORD'

DEBUG_APPS = (
    'django_extensions',
)
INTERNAL_IPS = ('127.0.0.1',)
INSTALLED_APPS += DEBUG_APPS
ALLOWED_HOSTS = ('*')