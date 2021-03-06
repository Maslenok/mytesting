"""
Django settings for mytesting project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from django.conf import settings


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z_(b!@k^4^v=db5b4#5o-)a367ylb=gmaxzb&hl1y#=&pe&$i$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



#TEMPALATES_DIRS = (
 #   "/home/maslenok/venv/django_project/git/mytesting/templates" , 
 #   "/home/maslenok/venv/django_project/git/mytesting/testing_code/templates/testing_code/",
  #  )

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
   # 'pilkit',
    'nested_admin',
    'core',
    'app.result',
    'app.testing',

]

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#if settings.DEBUG:
#    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)


#INTERNAL_IPS = ('127.0.0.1',)

#INSTALLED_APPS += ('debug_toolbar', )


# Настройка отправки писем и настройка почтового сервера

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL =    "  "       #'admin@enjoy-sa.ru'
EMAIL_HOST = ""                    # 'smtp.fullspace.ru'
EMAIL_HOST_USER =  ""              # 'admin@enjoy-sa.ru'
EMAIL_HOST_PASSWORD = ""           #'alena2010'


# TEMPLATE_CONTEXT_PROCESSORS

# from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP


#TEMPLATE_CONTEXT_PROCESSORS = TCP + (
#    'django.core.context_processors.request',
#    'core.context.site_setup',
#    'apps.seo.context.seo_setup',
#    'apps.ticket.context.travels',
#)


ROOT_URLCONF = 'mytesting.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
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

WSGI_APPLICATION = 'mytesting.wsgi.application'


# расширение модели User
AUTH_USER_MODEL = 'core.User'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databa
"""""
DATABASES = {
      'default': {
          'NAME': 'conector',
          'ENGINE': 'mysql.connector.django',
          'USER': 'root',
          'PASSWORD': 'Grum2132',
          'OPTIONS': {
            'autocommit': True,
          },
      }
  }



"""""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')



STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),

]

STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn")

MEDIA_ROOT = os.path.join(BASE_DIR,'static' , 'media')
MEDIA_URL = '/media/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'width': 700,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['FontSize', 'TextColor'],
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Image'],
            ['RemoveFormat', 'Source']
        ]
    },
}