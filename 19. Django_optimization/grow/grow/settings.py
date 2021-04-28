"""
Django settings for grow project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import json
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.conf.global_settings import EMAIL_USE_TLS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'in5dj6+25+5ob(da(asdc8pyb$f9$5hf!62#k!=)vs-@ptn3@2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp',
    'authapp',
    'basketapp',
    'adminapp',
    'social_django',
    'ordersapp',

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

if DEBUG:
    INSTALLED_APPS.extend(
        ['debug_toolbar',
         'template_profiler_panel',
         'django_extensions',
        ]
    )
    MIDDLEWARE.append(
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    )

    def show_toolbar(request):
        return True


    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda res:True,
    }

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
        'template_profiler_panel.panels.template.TemplateProfilerPanel',
    ]
ROOT_URLCONF = 'grow.urls'

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
                'mainapp.context_processors.categories',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'grow.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if not DEBUG:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'NAME': 'grow',
        'USER': 'django',
        'PASSWORD': 'geekbrains',
    }

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'authapp.GrowUser'
LOGIN_URL = '/auth/login/'

# Setting SMTP -server
DOMAIN_NAME = 'http://localhost:8000'
# Yandex-error
# EMAIL_HOST = 'smtp.yandex.ru'
# EMAIL_HOST_USER = 'django2.2@yandex.ru'
# EMAIL_HOST_PASSWORD = '*****'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'growyourselfadmin@test.ru'
# SERVER_EMAIL = 'growyourselfadmin@test.ru'

EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'djangoadmin@growyourself.local'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'geekshop')
EMAIL_USE_SSL = False

ACTIVATION_KEY_TTL = 48
# вариант python -m smtpd -n -c DebuggingServer localhost:25
# EMAIL_HOST_USER, EMAIL_HOST_PASSWORD = None, None

# вариант логирования сообщений почты в виде файлов
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tmp/email-messages/'

# Google+ auth
SOCIAL_AUTH_URL_NAMESPACE = 'social'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
)

obj = {}
with open('grow/secret.json', 'r') as file:
    obj = json.load(file)['web']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = obj.get('client_id', '')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = obj.get('client_secret', '')

# SETTING for get user_data from socialnetwork Google+

SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'email',
    'profile',
    'openid',
    'https://www.googleapis.com/auth/plus.login',
]

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.create_user',
    'authapp.pipeline.save_profile',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
#Used Cach to optimization
LOW_CACHE = False

if os.name == 'posix':
    CACHE_MIDDLEWARE_ALIAS = 'default'
    CACHE_MIDDLEWARE_SECONDS = 120
    CACHE_MIDDLEWARE_KEY_PREFIX = 'grow'

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }

    LOW_CACHE = True