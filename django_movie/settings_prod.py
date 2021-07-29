from pathlib import Path

from .settings_extra import CKEDITOR_CONFIGS

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '89u6nr5eb4vr-rvfw4vv3-fiw+p3a2i3vw4r-4r4wb(e=b7@_4*i1da74z#be5tr5be)*4tb45t45t'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DjangoMovie',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

STATIC_DIR = BASE_DIR / 'static'
STATICFILES_DIRS = (STATIC_DIR,)
STATIC_ROOT = BASE_DIR / 'static'
