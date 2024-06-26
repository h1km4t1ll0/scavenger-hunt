"""
Django settings for shelbyBot project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%8&a)j$$*52dz+dp_-94r5&ce9=u*o5r-yn11l3%1734#s&bvx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", False)
DOMAIN = os.environ.get("DOMAIN", None)

ALLOWED_HOSTS = [DOMAIN, '127.0.0.1', 'localhost', f'https://{DOMAIN}']
if not DEBUG:
    CSRF_TRUSTED_ORIGINS = [f'https://{DOMAIN}']

if os.environ.get("SERVER", '') in ["True", True]:
    CSRF_TRUSTED_ORIGINS = [f'https://{DOMAIN}']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shelbyBot'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shelbyBot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shelbyBot.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

if os.environ.get("SERVER", '') in ["True", True]:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get("DATABASE_NAME", ''),
            'USER': os.environ.get('DATABASE_USER', ''),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
            'HOST': os.environ.get('DATABASE_HOST', ''),
            'PORT': os.environ.get("DATABASE_PORT", ''),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = '/app/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

### SHELBY VARS ###
API_KEY: str = os.environ.get("API_KEY", '')
USER_TOKEN: str = os.environ.get("USER_TOKEN", '')
API_URL: str = os.environ.get("API_URL", '')
APP_ID: str = os.environ.get("APP_ID", '')
MY_STEAM_ID: str = os.environ.get("MY_STEAM_ID", '')
STEP_REF: int = int(os.environ.get("STEP_REF", 3))  # 3
STEP_KEY: int = int(os.environ.get("STEP_KEY", 5))  # 5
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", '')
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", '')

CELERY_BEAT_SCHEDULE = {
    'execute_every_ten_sec': {
        # 'task': 'shelbyBot.src.order.work_orders',
        'task': 'shelbyBot.tasks.work_orders',
        'schedule': 60.0,  # Run every 60 seconds (once a minute)
    },
}
