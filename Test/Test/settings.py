import os
import dj_database_url
from pathlib import Path
from django.contrib.messages import constants as message_constants

BASE_DIR = Path(__file__).resolve().parent.parent
CSRF_TRUSTED_ORIGINS= ["https://marketplace-production-3136.up.railway.app"]

# Use environment variable for secret key
SECRET_KEY = 'django-insecure-+cc7=5^@7#k$##3fc@m6q_9%x450vk#7mj5#__hz*&7q%jx@9p'

DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
    'items.apps.ItemsConfig',
    'deposit.apps.DepositConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'carts.apps.CartsConfig',
    'dashboard.apps.DashboardConfig',
    'inventory.apps.InventoryConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ← Required for static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'Test.wsgi.application'

# Use environment-provided database config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'gpcayHhqcytIiXTvaIByNARJOpTWiYdv',
        'HOST': 'turntable.proxy.rlwy.net',
        'PORT': '19684',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Cairo'
USE_I18N = True
USE_TZ = True


STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'Test/static')
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = '/home'

MESSAGE_TAGS = {
    message_constants.DEBUG: 'secondary',
    message_constants.INFO: 'info',
    message_constants.SUCCESS: 'success',
    message_constants.WARNING: 'warning',
    message_constants.ERROR: 'danger',
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
