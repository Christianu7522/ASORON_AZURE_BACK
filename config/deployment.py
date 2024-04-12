import os
from .settings import *
from .settings import BASE_DIR


SECRET_KEY = os.environ['SECRET']


ALLOWED_HOSTS = ['https://asoronv.z13.web.core.windows.net']
CSRF_TRUSTED_ORIGINS = ['https://asoronv.z13.web.core.windows.net']
DEBUG = False
MIDDLEWARE=[
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
DATABASES= {
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': os.environ['POSTGRES_PORT'],
        'OPTIONS': {
                'options': '-c search_path=cegomes'
         }
}
}
AWS_ACCESS_KEY_ID=os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY=os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME=os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_SIGNATURE_NAME=os.environ['AWS_S3_SIGNATURE_NAME']
AWS_S3_REGION_NAME=os.environ['AWS_S3_REGION_NAME']
EMAIL_HOST_USER=os.environ['EMAIL_HOST_USER']
EMAIL_PORT=os.environ['EMAIL_PORT']
EMAIL_HOST_PASSWORD=os.environ['EMAIL_HOST_PASSWORD']

CORS_ALLOW_ALL_ORIGINS=False
CORS_ALLOWED_ORIGIN_REGEXES = [
    'https://asoronv.z13.web.core.windows.net'
]