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

# SECURITY WARNING: don't run with debug turned on in production!  Turning this off disables my static content.
DEBUG = False

#TO DO, want to have actual URLs not the AWS long address for allowed hosts.  When live, remove the local IPs
ALLOWED_HOSTS = ['localhost', 'hopewellhockey.com', '127.0.0.1', '35.166.72.216']

# Hopewell Hockey App definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'axes',
    'captcha',
    'easy_timezones',
    'djangobower',
    'functional_tests',
    'hhockeyUser',
    'staticContent',
    'webpack_loader',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sites',
    'django_nose',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    'django_jenkins',


]

SITE_ID = 2

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

#'hhockeyUser.middleware.LoginRequiredMiddleware',

#https - change hsts to 31536000 once tested
'''
if DEBUG == False:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
'''

#Axes config
AXES_LOGIN_FAILURE_LIMIT = 7
AXES_COOLOFF_TIME = 2
AXES_LOCKOUT_URL = reverse_lazy('locked_page')

LOGIN_EXEMPT_URLS = (

)
#r'^$',
ROOT_URLCONF = 'hhockey.urls'

##################
# AUTHENTICATION #
##################


AUTH_USER_MODEL = "hhockeyUser.User"

LOGIN_REDIRECT_URL = reverse_lazy('home_page')
LOGIN_URL = reverse_lazy('customer:login')
LOGOUT_URL = reverse_lazy('customer:logout')

ACCOUNT_SIGNUP_FORM_CLASS = 'oscar.apps.customer.forms.EmailUserCreationForm'

SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'METHOD': 'oauth2',
        'VERIFIED_EMAIL': False,
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERSION': 'v2.8'
    },
    'twitter': {}
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'oscar.apps.customer.auth_backends.Emailbackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
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

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


# Email settings
email_host = get_secret("EMAIL_HOST")
email_host_user = get_secret("EMAIL_HOST_USER")
email_to_user = get_secret("EMAIL_TO_USER")
email_host_password = get_secret("EMAIL_HOST_PASSWORD")

# Can change the stmp part to console in order to test the email output.
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = email_host
EMAIL_HOST_USER = email_host_user
EMAIL_HOST_PASSWORD = email_host_password
DEFAULT_FROM_EMAIL = email_to_user
DEFAULT_TO_EMAIL = email_to_user
SERVER_EMAIL = email_host_user
EMAIL_PORT = 465
EMAIL_USE_SSL = True


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
BOWER_COMPONENTS_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../static'))


# Static files (CSS, JavaScript, Images)

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../../static'))
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../../media'))

MEDIA_URL = '/media/'

STATICFILES_DIRS = [
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
        'STATS_FILE': os.path.join(BASE_DIR + '../static/app/js', 'webpack-stats.json'),
    }
}

#########################
# LOGGING               #
#########################

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
        'hhockeyUser': {
            'handlers': ['console'],
        },
        'staticContent': {
            'handlers': ['console'],
        },
        'oscarCustom': {
            'handlers': ['console'],
        },

    },
    'root': {'level': 'INFO'},
}

#########################
# oscar modifications   #
#########################

from oscar.defaults import *
from oscar import OSCAR_MAIN_TEMPLATE_DIR
from oscar import get_core_apps

location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', x)

TEMPLATES[0]['DIRS'] = [
    location('templates'),
    OSCAR_MAIN_TEMPLATE_DIR,
    os.path.join(BASE_DIR, 'templates'),
]

TEMPLATES[0]['OPTIONS']['context_processors'] += [
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.core.context_processors.metadata',
]

INSTALLED_APPS += [
    'django.contrib.flatpages',
    'compressor',
    'widget_tweaks',
    'oscarCustom',
] + get_core_apps(['oscarCustom.promotions',
                   'oscarCustom.catalogue',
                   'oscarCustom.customer',
                   'oscarCustom.basket',
                   'oscarCustom.checkout',
                   'oscarCustom.catalogue.reviews'])


MIDDLEWARE_CLASSES += [
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': location('whoosh_index'),
    },
}

OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}

OSCAR_ALLOW_ANON_CHECKOUT = False
OSCAR_DEFAULT_CURRENCY = 'USD'
OSCAR_CURRENCY_LOCALE = 'da'
OSCAR_CURRENCY_FORMAT = '$ ###'

OSCAR_SHOP_NAME = 'Hopewell Hockey'
OSCAR_ACCOUNTS_REDIRECT_URL = 'customer:profile-view'

# Registration
OSCAR_SEND_REGISTRATION_EMAIL = True
OSCAR_FROM_EMAIL = 'info@hopewellhockey.com'

#other settings
OSCAR_ALLOW_ANON_REVIEWS = False

# =================
# Stripe settings
# =================

LSK = get_secret("LIVE_SECRET_KEY")
LPK = get_secret("LIVE_PUBLISH_KEY")

STRIPE_SECRET_KEY = LSK
STRIPE_PUBLISHABLE_KEY = LPK
STRIPE_CURRENCY = 'USD'


