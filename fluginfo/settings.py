"""
Django settings for fluginfo project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import amadeus_connector as ac

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'not relevant'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('FLUGINFO_BACKEND_DEBUG', 'false') == 'true'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    os.environ.get('FLUGINFO_BACKEND_HOSTNAME', 'localhost'),
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    fr'^http(s)?://{os.environ.get("FLUGINFO_BACKEND_FRONTEND_HOSTNAME", "localhost")}(:[0-9]+)?$',
    r'^http(s)?://localhost(:[0-9]+)?$'
]

CORS_ALLOW_CREDENTIALS = True

CSP_FRAME_SRC = (os.environ.get(
    'FLUGINFO_BACKEND_FRONTEND_HOSTNAME', 'localhost'), )
CSP_FRAME_ANCESTORS = (os.environ.get(
    'FLUGINFO_BACKEND_FRONTEND_HOSTNAME', 'localhost'), )
CSP_SCRIPT_SRC = ('cdn.jsdelivr.net', "'unsafe-inline'", )
CSP_STYLE_SRC = ('cdn.jsdelivr.net', "'unsafe-inline'", )
CSP_IMG_SRC = ("'self'", "'unsafe-inline'",
               'cdn.jsdelivr.net', 'blob:', 'data:', )
CSP_MEDIA_SRC = ("'self'", 'data:', )

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_spectacular',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]

ROOT_URLCONF = 'fluginfo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'fluginfo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Fluginfo API',
    'DESCRIPTION': 'API to query information about flights.',
    'VERSION': 'v1.0',
}

AMADEUS_KEY = os.environ.get('FLUGINFO_BACKEND_AMADEUS_API_KEY')
AMADEUS_SECRET = os.environ.get('FLUGINFO_BACKEND_AMADEUS_API_SECRET')

AIRHEX_KEY = os.environ.get('FLUGINFO_BACKEND_AIRHEX_API_KEY', '')

CACHE_TIMEOUT = 0 if DEBUG else 1800

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'cache_table',
        'OPTIONS': {
            'MAX_ENTRIES': 5000,
        },
        'TIMEOUT': CACHE_TIMEOUT,
    }
} if not DEBUG else {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
}

AMADEUS_PROD = os.environ.get(
    'FLUGINFO_BACKEND_AMADEUS_PROD', 'false') == 'true'

ac.set_cache_timeout(CACHE_TIMEOUT)  # CACHE_TIMEOUT
amadeus_connector = ac.AmadeusConnector(
    client_id=AMADEUS_KEY,
    client_secret=AMADEUS_SECRET,
    prod=AMADEUS_PROD,
    debug=DEBUG,
    debug_output_path=os.path.join(BASE_DIR, 'amadeus_connector'),
)
