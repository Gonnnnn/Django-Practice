"""
Django settings for customUser_SocialLogin project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import json
import sys
from django.utils import timezone


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take confidential data from this file
SECRET_BASE_FILE = os.path.join(BASE_DIR, 'secrets.json')
secrets = json.loads(open(SECRET_BASE_FILE).read())
for key, value in secrets.items():
    setattr(sys.modules[__name__], key, value)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets['SECRET_KEY']
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # new

    'rest_framework', # new
    # auth token 발행. 사이트 내부적으로 가입할때 toeken
    # 우린 JWT쓰니까 필요 없는데 ALLAUTH쓸때 오류 안나려고 넣어줘야하는거같음
    'rest_framework.authtoken', # new
    # 'rest_framework_jwt',
    'rest_framework_simplejwt.token_blacklist',
    # 'dj_rest_auth',
    # 'dj_rest_auth.registration',

    'allauth', # new
    'allauth.account', # new 
    'allauth.socialaccount', # new
    'allauth.socialaccount.providers.google',
    
    # REACT 서버 접속
    'corsheaders', # new
    
    'django_extensions',
    # CUSTOM APP
    'users',
]

SITE_ID = 1
AUTH_USER_MODEL = 'users.User'
TIME_ZONE = 'Asia/Seoul'
USE_TZ = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # To access REACT server
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'customUser_SocialLogin.urls'

# Django All Auth config
# 아마 고쳐져야할것
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend", "allauth.account.auth_backends.AuthenticationBackend",
)


# Provider specific settings
google_client_id = secrets['SOCIAL_AUTH_GOOGLE_CLIENT_ID']
google_secret = secrets['SOCIAL_AUTH_GOOGLE_SECRET']
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': google_client_id,
            'secret': google_secret,
            'key': ''
        }
    }
}

# Rest Framework config. Add all of this.
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# google login
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_EMAIL_VERIFICATION = False

# ACCOUNT_SESSION_REMEMBER = True
# ACCOUNT_USERNAME_REQUIRED = False

# # 뭘로 로그인 가능한지
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
# 그외에 찾ㅇㄴ 쓸만한 config

# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_PASSWORD_MIN_LENGTH = 8

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timezone.timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timezone.timedelta(hours=6),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
}


# https://dev-yakuza.posstree.com/ko/django/jwt/

REST_USE_JWT = True
JWT_AUTH_RETURN_EXPIRATION = True
# JWT_AUTH = {
#     'JWT_SECRET_KEY': SECRET_KEY,
#     'JWT_ALGORITHM': 'HS256',
#     'JWT_ALLOW_REFRESH': True,
#     'JWT_EXPIRATION_DELTA': timezone.timedelta(minutes=3),
#     'JWT_REFRESH_EXPIRATION_DELTA': timezone.timedelta(minutes=3),
# }

# Specifies localhost port 3000 where the React
# server will be running is safe to receive requests
# from. All all of this.
CORS_ALLOWED_ORIGINS = [    
'http://localhost:3000'
]


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

WSGI_APPLICATION = 'customUser_SocialLogin.wsgi.application'


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
