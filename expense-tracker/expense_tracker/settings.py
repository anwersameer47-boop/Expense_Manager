"""
Django settings for expense_tracker project.

Beginner-friendly settings for the Expense Tracker Web Application.
"""

import os
from pathlib import Path

# -------------------------------------------------------------------
# Base Directory
# -------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------------
# Security Settings
# -------------------------------------------------------------------
# IMPORTANT: In production, keep the secret key secret!
SECRET_KEY = 'django-insecure-expense-tracker-secret-key-change-in-production'

# Set to False in production
DEBUG = True

# Allow all hosts (required for Replit deployment)
ALLOWED_HOSTS = ['*']

# -------------------------------------------------------------------
# Installed Applications
# -------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',          # Admin panel
    'django.contrib.auth',           # Built-in authentication
    'django.contrib.contenttypes',   # Content types framework
    'django.contrib.sessions',       # Session management
    'django.contrib.messages',       # Flash messages
    'django.contrib.staticfiles',    # Static files handling
    'expenses',                      # Our custom expense tracking app
]

# -------------------------------------------------------------------
# Middleware
# -------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------------------------------------------------
# URL Configuration
# -------------------------------------------------------------------
ROOT_URLCONF = 'expense_tracker.urls'

# -------------------------------------------------------------------
# Templates Configuration
# -------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Global templates folder
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

# -------------------------------------------------------------------
# WSGI Application
# -------------------------------------------------------------------
WSGI_APPLICATION = 'expense_tracker.wsgi.application'

# -------------------------------------------------------------------
# Database — SQLite (beginner-friendly, no setup required)
# -------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------------------------------------------------
# Password Validation
# -------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------------------------------------------------
# Internationalization
# -------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------------------------------------------------
# Static Files (CSS, JavaScript, Images)
# -------------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Custom static files folder
STATIC_ROOT = BASE_DIR / "staticfiles"

# -------------------------------------------------------------------
# Default Primary Key Field
# -------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------------------------------------------------
# Authentication Redirects
# -------------------------------------------------------------------
LOGIN_URL = '/login/'               # Redirect here if not logged in
LOGIN_REDIRECT_URL = '/dashboard/'  # Redirect here after successful login
LOGOUT_REDIRECT_URL = '/'          # Redirect here after logout

# -------------------------------------------------------------------
# CSRF Trusted Origins (for Replit)
# -------------------------------------------------------------------
CSRF_TRUSTED_ORIGINS = [
    'https://*.replit.dev',
    'https://*.repl.co',
    'https://*.replit.app',
]
