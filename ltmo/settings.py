# -*- coding: utf-8 -*-

import os
DEBUG = True

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

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

AUTH_PROFILE_MODULE = 'auth.User'

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookBackend',
    'social.backends.google.GoogleBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/~'

REGISTRATION_BACKEND = 'registration.backends.default.DefaultBackend'

SOCIAL_AUTH_CREATE_USERS = True

SOCIAL_AUTH_FORCE_RANDOM_USERNAME = False

LOGIN_ERROR_URL = '/login/error/'

SOCIAL_AUTH_ERROR_KEY = 'socialauth_error'

SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook', 'google')

SOCIAL_AUTH_COMPLETE_URL_NAME = 'socialauth_complete'

SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'associate_complete'

SOCIAL_AUTH_DEFAULT_USERNAME = lambda u: slugify(u)

SOCIAL_AUTH_EXTRA_DATA = False

SOCIAL_AUTH_CHANGE_SIGNAL_ONLY = True

SOCIAL_AUTH_ASSOCIATE_BY_MAIL = True

ACCOUNT_ACTIVATION_DAYS = 2

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
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.static',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
 
            ],
        },
    },
]
 

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
    'social.apps.django_app.default',
    'debug_toolbar',
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
