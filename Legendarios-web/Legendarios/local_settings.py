# Settings used for development only
import os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

DATABASES = {
    'default': {
        # Config for local dev with SQLite3
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'registros_legendarios',
        'USER': 'legendarios',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
