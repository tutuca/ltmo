# -*- coding: utf-8 -*-
import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('etnalubma', 'francisco.herrero@gmail.com'),
    ('tutuca', 'maturburu@gmail.com'),
    ('ewock', 'onetti.martin@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ltmo',                      # Or path to database file if using sqlite3.
        'USER': 'ltmo',                      # Not used with sqlite3.
        'PASSWORD': 'lossiswin',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'gn' # Using Guarani, Of Course

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = ''

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = 'admin_media/'
SECRET_KEY = '7$57#ttr-tzqr*dt$l7vac0xt&1+i=gi^-y8bnsba$i%ci^nrd'


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'ltmo.urls'

TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',)

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'))

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django_markdown2',
    'tagging',
    'ltmo'    
)
