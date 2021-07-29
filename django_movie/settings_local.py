from pathlib import Path

from .settings_extra import CKEDITOR_CONFIGS

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-fiw+p3a2i3$-ejx*vm(e=b7@_4*i1da74z#8vscpfe)*brrheq'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_DIR = BASE_DIR / 'static'
STATICFILES_DIRS = (STATIC_DIR,)
