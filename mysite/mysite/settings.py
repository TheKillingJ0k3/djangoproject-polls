"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""


#TUTORIAL https://docs.djangoproject.com/en/4.0/intro/tutorial02/

# venv
# pip install -r requirements.txt
# django-admin startproject mysite
# python manage.py startapp polls

# cd ~/th3ki11ingj0k3.pythonanywhere.com
# configure app from github to pythonanywhere: $ pa_autoconfigure_django.py --python=3.8 https://github.com/<your-github-username>/my-first-blog.git
# activate venv: myvenv\Scripts\activate
# starting web server: python manage.py runserver
# create the tables in the database python manage.py migrate (looks at the INSTALLED_APPS setting and creates any necessary database tables)
# python manage.py makemigrations polls
# python manage.py sqlmigrate polls 0001 -- The sqlmigrate command takes migration names and returns their SQL
# python manage.py migrate to create those model tables in your database

# model changes:

# Change your models (in models.py).
# Run python manage.py makemigrations to create migrations for those changes
# Run python manage.py migrate to apply those changes to the database.

# play with API - python manage.py shell (manage.py sets the DJANGO_SETTINGS_MODULE environment variable,
# which gives Django the Python import path to your mysite/settings.py file)
# play around with queries
# create admin user python manage.py createsuperuser ggpat/ggpat/PH@1gr
#  we need to tell the admin that Question objects have an admin interface. To do this, open the polls/admin.py file

#initialize git repo


from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$4_9&72crm%%0m9)+_-w^x%wkd08@^s4efc33w6wkji*4()c(g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [ # some make use of db tables, so we need to create the tables in the database before we can use them
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Athens'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'