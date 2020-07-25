import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '_lvq0wwssgs*i5q^#rw@rbus=m2*v9h7$5s^w)wjxqdzj1psy9'

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'lyrics',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

from .settings import INSTALLED_APPS

INSTALLED_APPS += ['rest_framework', 'webapp']

LOGOUT_REDIRECT_URL = '/login/'

SEND_ACTIVATION_EMAIL = True
ACCOUNT_ACTIVATION_DAYS = 30
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# uncomment below in development
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# use in deployment
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')