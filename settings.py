# Django settings for audio project.
import os
from sifre import KEY

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Refik Turkeli', 'refik.rfk@gmail.com'),
)

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'tr-tr'

LANGUAGES = (
    ('en', 'English'),
    ('tr', 'Turkish'),
)

SITE_ID = 2

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

AUTH_PROFILE_MODULE = 'calisanProfil.CalisanProfil'

STATIC_URL = '/statik/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_PATH + '/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '127.0.0.1:8000' + STATIC_URL

FILEBROWSER_MEDIA_ROOT = PROJECT_PATH + '/statik/'

FILEBROWSER_MEDIA_URL = '/statik/'

FILEBROWSER_DIRECTORY = 'yukleme/'

FILEBROWSER_URL_FILEBROWSER_MEDIA = STATIC_URL + 'filebrowser/'

FILEBROWSER_PATH_FILEBROWSER_MEDIA = '/home/refik/code/pythonenv/audio/lib/python2.6/site-packages/django_filebrowser-3.3.0-py2.6.egg/filebrowser/static/filebrowser'

FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'upscale'},
    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'urun_ufak': {'verbose_name': 'Urun Ufak', 'width': 190, 'height': 190, 'opts': 'upscale'},
    'panel_ufak': {'verbose_name': 'Panel Ufak', 'width': '', 'height': '110', 'opts': 'upscale'},
    'urun': {'verbose_name': 'Urun', 'width': 430, 'height': 430, 'opts': 'upscale'},
    'haber_ufak': {'verbose_name': 'Haber Ufak', 'width': 55, 'height': 55, 'opts': 'upscale'},
    'yeni_ufak': {'verbose_name': 'Yeni Ufak', 'width': 65, 'height': 65, 'opts': 'upscale'},
    'dokuman_ufak': {'verbose_name': 'Dokuman Ufak', 'width': 60, 'height': 60, 'opts': 'upscale'},
    'diger_model': {'verbose_name': 'Diger Model', 'width': 145, 'height': 145, 'opts': 'upscale'},
    'sistem_ufak': {'verbose_name': 'Sistemin Ufak Logosu', 'width': 110, 'height': 110, 'opts': 'upscale'},
    'kalite_belgesi' : {'verbose_name': 'Kalite Belgesi', 'width': 300, 'height': 300, 'opts': 'upscale'},
    'kucuk' : {'verbose_name': 'Kucuk', 'width': 100, 'height': 100, 'opts': 'upscale'},
    'orta' : {'verbose_name': 'Orta', 'width': 200, 'height': 200, 'opts': ''},
    'buyuk' : {'verbose_name': 'Buyuk', 'width': 300, 'height': 300, 'opts': ''},
    'tam' : {'verbose_name': 'Tam', 'width': 400, 'height': 400, 'opts': ''},

}

FILEBROWSER_MAX_UPLOAD_SIZE = 10000000000000000000

FILEBROWSER_ADMIN_VERSIONS = ['kucuk', 'orta', 'buyuk', 'tam']

GRAPPELLI_INDEX_DASHBOARD = 'audio.dashboard.CustomIndexDashboard'

GRAPPELLI_ADMIN_TITLE = 'Audio Elektronik Web Sitesi Kontrol Paneli'

FEINCMS_ADMIN_MEDIA = '/statik/feincms/'
# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'

#STATICFILES_FINDERS = (
#    "django.contrib.staticfiles.finders.FileSystemFinder",
#    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
#)

STATICFILES_DIRS = (
    PROJECT_PATH + '/statik',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = KEY

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'audio.ortakVeri.icerik_islemci.afis.afis',
    'audio.ortakVeri.icerik_islemci.menu.menu',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'audio.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_PATH + '/sablon',
)

COMMENTS_APP = 'audio.teklif'

INSTALLED_APPS = (
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    'django.contrib.sitemaps',
    'audio.ozelSayfa',
    'audio.ortakVeri',
    'audio.haber',
    'audio.urun',
    'audio.bilgiGiris',
    'audio.calisanProfil',
    'audio.dokuman',
    'audio.bilgiTakip',
    'audio.teklif',
    'feincms',
    'mptt',
    'south',
)
