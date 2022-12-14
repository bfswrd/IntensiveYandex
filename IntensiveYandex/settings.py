import os
from pathlib import Path

from django_cleanup.signals import cleanup_pre_delete
from dotenv import find_dotenv, load_dotenv
from sorl.thumbnail import delete


def sorl_delete(**kwargs):
    delete(kwargs["file"])


cleanup_pre_delete.connect(sorl_delete)

# Config

load_dotenv(find_dotenv())

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", default="BFSWRD")

DEBUG = os.getenv("DEBUG", default="False").lower() in ["on", "true"]

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", default="127.0.0.1").split(",")

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.utils.timezone",

    "about.apps.AboutConfig",
    "catalog.apps.CatalogConfig",
    "homepage.apps.HomepageConfig",
    "feedback.apps.FeedbackConfig",
    "users.apps.UsersConfig",
    "rating.apps.RatingConfig",
    "Core.apps.CoreConfig",

    "django_summernote",
    "sorl.thumbnail",
    "django_cleanup.apps.CleanupConfig",
    "debug_toolbar",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "IntensiveYandex.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

                "Core.context_processors.birthday.birthday_users",
            ],
        },
    },
]

WSGI_APPLICATION = "IntensiveYandex.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = "static"
STATICFILES_DIRS = [
    BASE_DIR / "static_dev",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

NOREPLY_EMAIL = os.environ["NOREPLY_EMAIL"]
ADMIN_EMAILS = os.environ["ADMIN_EMAILS"].split(",")

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / "send_mail"

LOGIN_URL = "/"
LOGIN_REDIRECT_URL = "/users/profile"
LOGOUT_REDIRECT_URL = "/users/login"

AUTH_USER_MODEL = "users.User"
