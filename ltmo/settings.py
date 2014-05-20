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
        'TEST_NAME': os.path.join(BASE_DIR, 'test_ltmo.db'),
    }
}

SOUTH_TESTS_MIGRATE = False

ALLOWED_HOSTS = []

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

AUTH_PROFILE_MODULE = 'auth.User'
LOGIN_REDIRECT_URL = '/~'

ACCOUNT_ACTIVATION_DAYS = 2
SECRET_KEY = '7$57#ttr-tzqr*dt$l7vac0xt&1+i=gi^-y8bnsba$i%ci^nrd'

PAGINATION_DEFAULT_WINDOW = 2

FORCE_LOWERCASE_TAGS = True

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOpenId',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_DIRS = (
    'templates',
    os.path.join(BASE_DIR, 'templates')
)

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

LOGIN_URL = '/login'
LOGOUT_URL = '/logout'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'social.apps.django_app.default',
    'registration',
    'debug_toolbar',
    'south',
    'endless_pagination',
    'taggit',
    'taggit_templatetags',
    'banners',
    'leaks',
)

try:
    from local_settings import *
except ImportError:
    pass
