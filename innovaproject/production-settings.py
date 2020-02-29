import dj_database_url
from .settings import *

DEBUG=False
TEMPLATE_DEUG=False
DATABASES['default'] = dj_database_url.config()
MIDDLEWARE+=['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
SECRET_KEY = 'n$i73dz)qq9-@4de)erk^%^d#7z7c4da$uw5!2+&dh10p&$&07'
ALLOWED_HOSTS = ['innova-ci.herokuapp.com']