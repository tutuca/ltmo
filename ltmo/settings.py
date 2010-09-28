# -*- coding: utf-8 -*-
import os
DEBUG = True

TEMPLATE_DEBUG = DEBUG

BASE_DIR = os.path.dirname(__file__)

ADMINS = (
    ('etnalubma', 'francisco.herrero@gmail.com'),
    ('tutuca', 'maturburu@gmail.com'),
    ('ewock', 'onetti.martin@gmail.com'),
)

MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'ltmo.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'gn' # Using Guarani, Of Course

SITE_ID = 1

USE_I18N = True

USE_L10N = True

ROOT_URLCONF = 'ltmo.urls'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = '7$57#ttr-tzqr*dt$l7vac0xt&1+i=gi^-y8bnsba$i%ci^nrd'

PAGINATION_DEFAULT_WINDOW = 2

FORCE_LOWERCASE_TAGS = True



MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'ltmo.context_processors.about',
)

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'))

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django_markdown2',
    'pagination',
    'tagging',
    'ltmo'    
)
from local_settings import *
