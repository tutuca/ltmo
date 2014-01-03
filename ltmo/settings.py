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
REGISTRATION_BACKEND = 'registration.backends.default.DefaultBackend'
SOCIAL_AUTH_CREATE_USERS          = True
SOCIAL_AUTH_FORCE_RANDOM_USERNAME = False
LOGIN_ERROR_URL                   = '/login/error/'
SOCIAL_AUTH_ERROR_KEY             = 'socialauth_error'
SOCIAL_AUTH_ENABLED_BACKENDS=('facebook', 'google')
SOCIAL_AUTH_COMPLETE_URL_NAME='socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME='associate_complete'
SOCIAL_AUTH_DEFAULT_USERNAME= lambda u: slugify(u)
SOCIAL_AUTH_EXTRA_DATA=False
SOCIAL_AUTH_CHANGE_SIGNAL_ONLY=True
SOCIAL_AUTH_ASSOCIATE_BY_MAIL=True

ACCOUNT_ACTIVATION_DAYS = 2
SECRET_KEY = '7$57#ttr-tzqr*dt$l7vac0xt&1+i=gi^-y8bnsba$i%ci^nrd'

PAGINATION_DEFAULT_WINDOW = 2

FORCE_LOWERCASE_TAGS = True

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleBackend',
    'django.contrib.auth.backends.ModelBackend',
)

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
    'social_auth.context_processors.social_auth_backends',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_DIRS = (
    'templates',
    os.path.join(BASE_DIR, 'templates')
)

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
    'registration',
    'social_auth',
    'debug_toolbar',
    'south',
    'pagination',
    'tagging',
    'banners',
    'ltmo',
)
# XXX: Remove this 
# Modify temporarily the session serializer because the json serializer in
# Django 1.6 can't serialize openid.yadis.manager.YadisServiceManager objects
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

try:
    from local_settings import *
except ImportError:
    pass
