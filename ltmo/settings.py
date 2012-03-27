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
        'NAME': os.path.join(BASE_DIR, 'ltmo.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'es-AR' # Using Guarani, Of Course

SITE_ID = 1

USE_I18N = True

USE_L10N = True

ROOT_URLCONF = 'ltmo.urls'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

UPLOAD_DIR = os.path.join(MEDIA_ROOT, 'upload')

UPLOAD_URL = 'http://i.ltmo'

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


SECRET_KEY = '7$57#ttr-tzqr*dt$l7vac0xt&1+i=gi^-y8bnsba$i%ci^nrd'

PAGINATION_DEFAULT_WINDOW = 2

FORCE_LOWERCASE_TAGS = True

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_DIRS = (
    'templates',
    os.path.join(BASE_DIR, 'templates')
)

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

LOGIN_URL = '/login'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.markup',
    'django.contrib.messages',
    'debug_toolbar',
    'south',
    'pagination',
    'tagging',
    'banners',
    'ltmo',
)

try:
    from local_settings import *
except ImportError:
    pass
