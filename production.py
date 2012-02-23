# Django settings for riverstudies project.
from settings import *
import json

with open('/app/conf/environment.json') as f:
    env = json.load(f)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

TEMPLATE_DIRS = (
        '/app/riverstudies/templates'
        )

MEDIA_URL = '/app/media/'
STATIC_URL = '/app/static/'

ROOT_URLCONF = 'urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env['DB_NAME'],
        'USER': env['DB_USER'],
        'PASSWORD': env['DB_PASSWORD'],
        'HOST': env['DB_HOST'],
        'PORT': env['DB_PORT'],
    }
}
