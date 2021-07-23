"""
Django settings for django_movie project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/

Файл со всеми настройками проекта
"""

from pathlib import Path

from .other_settings import CKEDITOR_CONFIGS

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Построение пути к корню проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fiw+p3a2i3$-ejx*vm(e=b7@_4*i1da74z#8vscpfe)*brrheq'

# SECURITY WARNING: don't run with debug turned on in production!
# Режим отладки проекта
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
# Активные приложения
INSTALLED_APPS = [
    # Перевод контента, приложение для создания мультиязычного сайта
    'modeltranslation',

    # Системные приложения (по умолчанию)
    # Сайт администрирования
    'django.contrib.admin',
    # Подсистема аутентификации
    'django.contrib.auth',
    # Подсистема для работы с типами объектов
    'django.contrib.contenttypes',
    # Подсистема сесий
    'django.contrib.sessions',
    # Подсистема сообщений
    'django.contrib.messages',
    # Подсистема для управления статическим содержимым сайта
    'django.contrib.staticfiles',

    # Системные приложения (доп.)
    # Для генерации простых-статичных страниц и django-allauth
    'django.contrib.sites',
    'django.contrib.flatpages',

    # Сторонние библиотеки
    'ckeditor',
    'ckeditor_uploader',  # для загрузки фалов через ckeditor
    'snowpenguin.django.recaptcha3',  # reCAPTCHA3
    'allauth',  # авторизация и регистрация через allauth
    'allauth.account',  # авторизация и регистрация
    'allauth.socialaccount',  # через соц.сети
    'allauth.socialaccount.providers.vk',  # через ВК

    # Мои приложения
    'movies.apps.MoviesConfig',
    'contact.apps.ContactConfig',
]
# Список подключённых промежуточных слоёв.
# Есть зависимость от порядка расположения в списке
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Следит за CSRF токенами
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Простые страницы
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # Для перевода страниц
    'django.middleware.locale.LocaleMiddleware',
]
# Указывает на модуль с корневыми шаблонами приложения
ROOT_URLCONF = 'django_movie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,  # стоит ли искать шаблоны в приложениях?
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

WSGI_APPLICATION = 'django_movie.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# Словарь с настройками для всех баз данных проекта
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Бэкенды проекта
AUTHENTICATION_BACKENDS = (
    # Бекэнд для авторизации через allauth
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

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
# Код языка (по умолчанию)
LANGUAGE_CODE = 'ru'
# Временная зона (по умолчанию)
TIME_ZONE = 'Europe/Minsk'

USE_I18N = True

USE_L10N = True
# Необходимость поддержки временных зон
USE_TZ = True

# Для авторизации/регистрации/аутентификации. Django-allauth
LOGIN_REDIRECT_URL = '/'  # перенаправление после входа на сайт
# Количество дней для подтвеждения email-а
ACCOUNT_USERNAME_MIN_LENGTH = 4  # мин. кол-во символов для логина
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
# dummy - крутиться в консоле, для smtp заменить на smtp
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# Языки для перевода
gettext = lambda s: s
LANGUAGES = (
    ('ru', gettext('Russia')),
    ('en', gettext('English')),
)
# Путь к директории со статикой
LOCALE_PATHS = (BASE_DIR / 'locale',)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_DIR = BASE_DIR / 'static'
STATICFILES_DIRS = (STATIC_DIR,)
# STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'  # url - имя GET адреса
MEDIA_ROOT = BASE_DIR / 'media'  # директоря хранения медиа

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Путь для загружаемых файлов, через CKEditor
CKEDITOR_UPLOAD_PATH = "uploads/"

# reCAPTCHA
RECAPTCHA_PUBLIC_KEY = '6LcD8mcbAAAAAJkTO2f-TeRBiG322dawhupu89gx'
RECAPTCHA_PRIVATE_KEY = '6LcD8mcbAAAAAK0dJpOfFlM3swILvBQAyrHbabEg'
RECAPTCHA_DEFAULT_ACTION = 'generic'
RECAPTCHA_SCORE_THRESHOLD = 0.5

# Для генерации простых страниц и django-allauth
SITE_ID = 1
