import os
from pathlib import Path
from os import getenv, path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mgo0xcdbl^%t^^-^2g2es=vt$av_gw7kmzw@jcw0u627()i_lj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("DEBUG", False) != "False"
PROD = not DEBUG

ALLOWED_HOSTS = ['*']


# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

APPS = [
    "account.apps.AccountConfig",
    "core.apps.CoreConfig",
    "delivery.apps.DeliveryConfig",
]

THIRD_PARTY_APPS = [
    # 'django-htmx',
    'widget_tweaks',
    'celery',
    'django_celery_results',
    'django_celery_beat',
]

INSTALLED_APPS = DJANGO_APPS + APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------------------------------------------------------------------------------------------------------------------
# django-debug-toolbar

if DEBUG:
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    INTERNAL_IPS = [
        "127.0.0.1",
    ]
    INSTALLED_APPS += [
        "debug_toolbar",
    ]

# ---------------------------------------------------------------------------------------------------------------------
ROOT_URLCONF = 'app.urls'
AUTH_USER_MODEL = "account.Account"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'app.wsgi.application'

# CELERY_RESULT_BACKEND = 'django-db'
# CELERY_IMPORTS = (
#     'core.tasks',
# )
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

BROKER_URL = 'redis://:dKqs72RhtaPPYyfN@redis:6379/0'

# ---------------------------------------------------------------------------------------------------------------------
# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": getenv("POSTGRES_DB", "default"),
        "USER": getenv("POSTGRES_USER", "db_user"),
        "PASSWORD": getenv("POSTGRES_PASSWORD", "gk2ccPem87TVMvxKsCndcJyHyK5NPNUWkQXJXtwz5MyXeZjuMJPTeZkpECCT9uEZ"),
        "HOST": getenv("POSTGRES_HOST", "localhost"),
        "PORT": getenv("POSTGRES_PORT", 5432),
    }
}
# ---------------------------------------------------------------------------------------------------------------------


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'az'

TIME_ZONE = 'Asia/Baku'

USE_I18N = True

USE_TZ = True

# ---------------------------------------------------------------------------------------------------------------------
# Static files (CSS, JavaScript, Images)

STATIC_URL = "/static/"
if not DEBUG:
    STATIC_ROOT = path.join(BASE_DIR, "static")
else:
    STATICFILES_DIRS = [
        path.join(BASE_DIR, "static"),
    ]

MEDIA_ROOT = path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
# ---------------------------------------------------------------------------------------------------------------------

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis:6379/0")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BROKER", "redis://redis:6379/0")

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login'
LOGIN_URL = '/login'
