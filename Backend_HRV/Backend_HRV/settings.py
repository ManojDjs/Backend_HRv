"""
Django settings for Backend_HRV project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_(^i1dof4%&&vso=a#3v!#umix#^tflb8zrrigi$b1q9#0-4b#'

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
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'drf_registration',
    # 'Users'
]
# AUTH_USER_MODEL = 'Users.User'
AUTHENTICATION_BACKENDS = [
    'drf_registration.auth.MultiFieldsModelBackend',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
'rest_framework.authentication.SessionAuthentication',
    ],
'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser'
   ),
'DATETIME_FORMAT':"%d-%b-%Y-%I:%M%p",
'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Backend_HRV.urls'

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

WSGI_APPLICATION = 'Backend_HRV.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

#
# EMAIL_FROM = 'djsmanoj12345678910@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
#  # my gmail password
# EMAIL_BCC='djsmanoj0000@gmail.com'
EMAIL_HOST_USER='applicationwellbeing@gmail.com'
#   # my gmail username
EMAIL_HOST_PASSWORD = 'Djsmanoj@1866'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

DRF_REGISTRATION = {


    # User fields to register and response to profile
    'USER_FIELDS': (
        'id',
        'username',
        'email',
        'password',
        'first_name',
        'last_name',
        'is_active',
    ),
    'USER_READ_ONLY_FIELDS': (
        'is_superuser',
        'is_staff',
        'is_active',
    ),
    'USER_WRITE_ONLY_FIELDS': (
        'password',
    ),

    'USER_SERIALIZER': 'drf_registration.api.user.UserSerializer',

    # User verify field
    'USER_VERIFY_FIELD': 'is_active',

    # Activate user by toiken sent to email
    'USER_ACTIVATE_TOKEN_ENABLED': True,
    'USER_ACTIVATE_SUCSSESS_TEMPLATE': '',
    'USER_ACTIVATE_FAILED_TEMPLATE': '',
    'USER_ACTIVATE_EMAIL_SUBJECT': 'Activate your account',
    'USER_ACTIVATE_EMAIL_TEMPLATE': '',

    # Profile
    'PROFILE_SERIALIZER': 'drf_registration.api.profile.ProfileSerializer',
    'PROFILE_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    # Register
    'REGISTER_SERIALIZER': 'drf_registration.api.register.RegisterSerializer',
    'REGISTER_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'REGISTER_SEND_WELCOME_EMAIL_ENABLED': True,
    'REGISTER_SEND_WELCOME_EMAIL_SUBJECT': 'Welcome to the system',
    'REGISTER_SEND_WELCOME_EMAIL_TEMPLATE': '',

    # Login
    'LOGIN_SERIALIZER': 'drf_registration.api.login.LoginSerializer',
    'LOGIN_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],

    # For custom login username fields
    'LOGIN_USERNAME_FIELDS': [ 'email','username'],

    'LOGOUT_REMOVE_TOKEN': False,

    # Change password
    'CHANGE_PASSWORD_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'CHANGE_PASSWORD_SERIALIZER': 'drf_registration.api.change_password.ChangePasswordSerializer',

    # Reset password
    'RESET_PASSWORD_ENABLED': True,
    'RESET_PASSWORD_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],

    # Social register/login
    'FACEBOOK_LOGIN_ENABLED': False,
    'GOOGLE_LOGIN_ENABLED': False,

    # Set password in the case login by socials
    'SET_PASSWORD_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'SET_PASSWORD_SERIALIZER': 'drf_registration.api.set_password.SetPasswordSerializer',
}