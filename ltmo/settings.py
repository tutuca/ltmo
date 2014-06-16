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

SECRET_KEY = '7$57#ttr-tzqr*dt$l7vac0xt&1+i=gi^-y8bnsba$i%ci^nrd'
SITE_ID = 1

LANGUAGE_CODE = 'es-AR'  # Using Guarani, Of Course
USE_I18N = True
USE_L10N = True

ROOT_URLCONF = 'ltmo.urls'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
UPLOAD_DIR = os.path.join(MEDIA_ROOT, 'upload')
UPLOAD_URL = 'http://i.ltmo'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
AUTH_PROFILE_MODULE = 'auth.User'
LOGIN_REDIRECT_URL = '/~'
ACCOUNT_ACTIVATION_DAYS = 2

PAGINATION_DEFAULT_WINDOW = 2
FORCE_LOWERCASE_TAGS = True
AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOpenId',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'ltmo.middleware.profile_middleware.ProfileMiddleware'
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
    'ltmo',
    'registration',
    'debug_toolbar',
    'south',
    'endless_pagination',
    'taggit',
    'taggit_templatetags',
    'banners',
    'leaks',
)
TAGGIT_TAGCLOUD_MIN = 1.0
TAGGIT_TAGCLOUD_MAX = 0.6
LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '''%(levelname)s %(asctime)s %(module)s %(duration)s %(sql)s %(params)s %(message)s'''
        },
    },
    'handlers': {
        'error_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'formatter': 'verbose'
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        # 'django.request': {
        #     'handlers': ['error_file'],
        #     'level': 'INFO',
        #     'propagate': False,
        # },
        'django.db.backends': {
            'handlers': ['console'],
        }
    }
}
try:
    from local_settings import *
except ImportError:
    pass
