"""
Django settings for hhockey project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import json
import sys

from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse_lazy

from oscar.defaults import *
from oscar import OSCAR_MAIN_TEMPLATE_DIR
from oscar import get_core_apps

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#JSON Secret module
with open("secrets.json") as f:
    secrets = json.loads(f.read())

def get_secret(setting,secrets=secrets):
    '''
    Get secret variable or return an exception
    '''
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['heritage-hockey.com']

# Heritage Hockey App definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangobower',
    'functional_tests',
    'staticContent',
    'webpack_loader',
    'account.apps.AccountConfig',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    'compressor',
    'widget_tweaks',
] + get_core_apps(['oscarFork.order'])

SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'hhockey.urls'

#AllAuth values
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': False
    }
}


LOGIN_REDIRECT_URL = reverse_lazy('home_page')
LOGIN_URL = reverse_lazy('account:login')
LOGOUT_URL = reverse_lazy('account:logout')

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_SIGNUP_FORM_CLASS = 'account.forms.SignupForm'

SOCIAL_AUTH_FACEBOOK_KEY = get_secret("SOCIAL_AUTH_FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = get_secret("SOCIAL_AUTH_FACEBOOK_SECRET")

SOCIAL_AUTH_TWITTER_KEY = get_secret("SOCIAL_AUTH_TWITTER_KEY")
SOCIAL_AUTH_TWITTER_SECRET = get_secret("SOCIAL_AUTH_TWITTER_SECRET")

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_LOGIN_REDIRECT_URL = reverse_lazy('home_page')
SOCIAL_AUTH_LOGIN_URL = reverse_lazy('account:login')



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            OSCAR_MAIN_TEMPLATE_DIR

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'hhockey.wsgi.application'


DB_NAME = get_secret("DATABASE_NAME")
DB_USER = get_secret("DATABASE_USERNAME")
DB_PASSWORD = get_secret("DATABASE_PASSWORD")
DB_HOST = get_secret("DATABASE_HOST")
DB_PORT = get_secret("PORT")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

if 'test' in sys.argv or 'test_coverage' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'

# Email settings
email_host = get_secret("EMAIL_HOST")
email_host_user = get_secret("EMAIL_HOST_USER")
email_to_user = get_secret("EMAIL_TO_USER")
email_host_password = get_secret("EMAIL_HOST_PASSWORD")

# Can change the stmp part to console in order to test the email output.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = email_host
EMAIL_HOST_USER = email_host_user
EMAIL_HOST_PASSWORD = email_host_password
DEFAULT_FROM_EMAIL = email_host_user
DEFAULT_TO_EMAIL = email_to_user
SERVER_EMAIL = email_host_user
EMAIL_PORT = 587
#EMAIL_USE_TLS = True

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr',
        'INCLUDE_SPELLING': True,
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Bower Config
BOWER_COMPONENTS_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'static'))


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

#TODO Eventually use a static CDN to serve static from another server
STATIC_ROOT=os.path.abspath(os.path.join(BASE_DIR, '../static'))
MEDIA_ROOT=os.path.abspath(os.path.join(BASE_DIR, '../media'))

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    'static/',
]

STATICFILES_FINDERS = (
    'djangobower.finders.BowerFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

BOWER_INSTALLED_APPS = (
    'underscore',
    "font-awesome#4.3.0",
    'jquery',
    'bootstrap'

)

#Webpack for ReactJS
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR + '/static/app/js', 'webpack-stats.json'),
    }
}

# LOGGING
LOGGING = {
   'version': 1,
   'disable_existing_loggers': False,
   'handlers': {
       'console': {
           'level': 'DEBUG',
           'class': 'logging.StreamHandler',
       },
   },
   'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'account': {
            'handlers': ['console'],
        },
        'staticContent': {
            'handlers': ['console'],
        },
    },
    'root': {'level': 'INFO'},
}

#Oscar Order Pipeline
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}