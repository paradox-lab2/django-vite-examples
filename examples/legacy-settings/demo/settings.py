from pathlib import Path
from decouple import config


BASE_DIR = Path(__file__).resolve().parent

USE_TZ = True

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool) 

ROOT_URLCONF = "demo.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [],
            "debug": DEBUG,
        },
    },
]

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_vite",
    "demo",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Add any legacy django-vite settings
DJANGO_VITE_ASSETS_PATH = "/"
DJANGO_VITE_DEV_MODE = config("DJANGO_VITE_DEV_MODE", default=False, cast=bool)
DJANGO_VITE_DEV_SERVER_PORT = config("DJANGO_VITE_DEV_SERVER_PORT", default="5173")
DJANGO_VITE_DEV_SERVER_HOST = config("DJANGO_VITE_DEV_SERVER_HOST", default="localhost")

# Add the build.outDir from vite.config.js to STATICFILES_DIRS
# so that collectstatic can collect your compiled vite assets.
BUILD_VITE_OUTPUT_DIR = config("BUILD_VITE_OUTPUT_DIR")
STATICFILES_DIRS = [
    BUILD_VITE_OUTPUT_DIR
]