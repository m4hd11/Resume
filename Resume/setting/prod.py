from Resume.settings import *
import os
from decouple import config

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['mahdiiranpour.ir', 'www.mahdiiranpour.ir']


# Application definition

INSTALLED_APPS = []

SITE_ID = 2


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / 'statics',
]


SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.travelistaa.ir'
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True 
EMAIL_HOST_USER = config('EMAIL_DJANGO_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_DJANGO_PASSWORD')
DEFAULT_FROM_EMAIL = config('EMAIL_DJANGO_USER')