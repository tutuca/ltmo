# -*- coding: utf-8 -*-

from pathlib import Path

DEBUG = True

BASE_DIR = Path(__file__).parent

ADMINS = (
    ("etnalubma", "francisco.herrero@gmail.com"),
    ("tutuca", "maturburu@gmail.com"),
    ("ewock", "onetti.martin@gmail.com"),
)

MANAGERS = ADMINS

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.messages",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "debug_toolbar",
    "pagination",
    "tagging",
    "banners",
    "ltmo",
)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "ltmo.db",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

SITE_ID = 1
TIME_ZONE = "America/Argentina"
LANGUAGE_CODE = "es-AR"
USE_I18N = True
USE_L10N = True

ROOT_URLCONF = "ltmo.urls"

MEDIA_ROOT = BASE_DIR / "media"
UPLOAD_DIR = MEDIA_ROOT / "upload"
UPLOAD_URL = "http://i.ltmo"
MEDIA_URL = "/media/"
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
ADMIN_MEDIA_PREFIX = "/static/admin/"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

AUTH_PROFILE_MODULE = "auth.User"
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
GOOGLE_CLIENT_ID = ""
GOOGLE_CLIENT_SECRET = ""
# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        "APP": {
            "client_id": GOOGLE_CLIENT_ID,
            "secret": GOOGLE_CLIENT_SECRET,
            "key": "",
        }
    }
}

LOGIN_REDIRECT_URL = "/~"
LOGIN_ERROR_URL = "/login/error/"


ACCOUNT_ACTIVATION_DAYS = 2

SECRET_KEY = "7$57#ttr-tzqr*dt$l7vac0xt&1+i=gi^-y8bnsba$i%ci^nrd"

PAGINATION_DEFAULT_WINDOW = 2

FORCE_LOWERCASE_TAGS = True

MIDDLEWARE_CLASSES = (
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "pagination.middleware.PaginationMiddleware",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.core.context_processors.static",
                "social.apps.django_app.context_processors.backends",
                "social.apps.django_app.context_processors.login_redirect",
            ],
        },
    },
]


EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

LOGIN_URL = "/login"
LOGOUT_URL = "/logout"


try:
    from local_settings import *
except ImportError:
    pass
