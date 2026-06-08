"""
Django settings for aibx project.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6ug^2rwz!xns8f=4p2y%h64g-8%ec@v)w*2ikx^g1s3^y8b1g!'

# SECURITY WARNING: don't run with debug turned on in production!
# ലൈവ് ആക്കുമ്പോൾ തൽക്കാലം എററുകൾ കാണാൻ True വെക്കാം, സെറ്റപ്പായിക്കഴിഞ്ഞാൽ ഫ്രീലേറ്റർ False ആക്കണം.
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # WhiteNoise സ്റ്റാറ്റിക് ഫയലുകൾക്ക് വേണ്ടി ട്രാക്ക് ചെയ്യും
    'whitenoise.runserver_nostatic', 
    'django.contrib.staticfiles',
    'corsheaders',

    'my_portfolio',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise Middleware (ഇത് കൃത്യമായി SecurityMiddleware-ന് താഴെ തന്നെ വരണം)
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
ROOT_URLCONF = 'aibx.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'aibx.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# പ്രൊഡക്ഷനിൽ സ്റ്റാറ്റിക് ഫയലുകൾ ഒരുമിച്ച് കൂട്ടാൻ ഇത് നിർബന്ധമാണ്
STATIC_ROOT = BASE_DIR / 'staticfiles'

# വൈറ്റ് നോയിസ് സ്റ്റാറ്റിക് ഫയലുകൾ കംപ്രസ് ചെയ്യാൻ
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'