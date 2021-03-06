import os
import dj_database_url

WEBSITE_NAME = "aug-virtual-class-mvt"
# the name for the directory that the settings.py file is in
PROJECT_MAIN_APP_NAME = "virtual_class"


WEBSITE_GLOBAL_URL = f'{WEBSITE_NAME}.herokuapp.com'

# global or local, if it doesn't exists local is the default (helps with testing inside of travis)
database_status = os.getenv("DATABASE_STATUS") or "local"
# global or local
server_status = os.getenv("SERVER_STATUS") or "local"

# convert string to boolean
USE_S3 = (os.getenv("USE_S3") == "True")
USE_AWS_FOR_OFFLINE_USAGE = (os.getenv("USE_AWS_FOR_OFFLINE_USAGE") == "True")
DEBUG = (os.getenv("DEBUG") == "True")


LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY=os.getenv("DJANGO_SECRET_KEY")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #for aws s3 storage (for static files)
    'storages',

]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


ROOT_URLCONF = f'{PROJECT_MAIN_APP_NAME}.urls'

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

WSGI_APPLICATION = f'{PROJECT_MAIN_APP_NAME}.wsgi.application'


# Database

CORS_ORIGIN_ALLOW_ALL = True

if server_status == "local":
    ALLOWED_HOSTS = ["127.0.0.1", "0.0.0.0"]
    if database_status == "local":
        # # this approach (using postgres for testing) works inside of docker, it seems hard to run without the
        # # need of docker (i can't run it as postgres without docker existence for now)
        # DATABASES = {
        #     'default': {
        #         'ENGINE': 'django.db.backends.postgresql',
        #         'NAME': os.getenv("POSTGRES_DB"),
        #         'USER': os.getenv("POSTGRES_USER"),
        #         'PASSWORD': os.getenv("POSTGRES_PASSWORD"),
        #         'HOST': os.getenv("POSTGRES_HOST"),
        #         'PORT': os.getenv("POSTGRES_PORT"),
        #         # 'TEST': {
        #         #     'NAME': os.getenv("POSTGRES_TEST_DB"),
        #         # },
        #     }
        # }
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
    elif database_status == "global":
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.getenv("GLOBAL_POSTGRES_DB"),
                'USER': os.getenv("GLOBAL_POSTGRES_USER"),
                'PASSWORD': os.getenv("GLOBAL_POSTGRES_PASSWORD"),
                'HOST': os.getenv("GLOBAL_POSTGRES_HOST"),
                'PORT': os.getenv("GLOBAL_POSTGRES_PORT"),
            }
        }

    else:
        raise ValueError("database_status is not recognized.(try to use global or  local ")


elif server_status == "global":
    ALLOWED_HOSTS = ['*']
    if database_status == "global":
        DATABASES={}
        DATABASES['default'] = dj_database_url.config()
    else:
        raise("The website can't run a dev(local) database on a global server")

else:
    raise ValueError("server_status is not recognized.(try to use global or  local ")


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

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

DEFAULT_PATH = "images/"
DEFAULT_USER_PATH = os.path.join(DEFAULT_PATH, 'users')

# aws s3 settings
if USE_S3:
    # aws settings
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # s3 static settings
    AWS_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
else:

    if USE_AWS_FOR_OFFLINE_USAGE:

        AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
        AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
        AWS_DEFAULT_ACL = 'public-read'
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
        AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
        # s3 static settings
        STATIC_LOCATION = 'static'
        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
        STATICFILES_STORAGE = f'{PROJECT_MAIN_APP_NAME}.storage_backends.StaticStorage'
        # s3 public media settings
        PUBLIC_MEDIA_LOCATION = 'media'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
        DEFAULT_FILE_STORAGE = f'{PROJECT_MAIN_APP_NAME}.storage_backends.PublicMediaStorage'
        # s3 private media settings
        PRIVATE_MEDIA_LOCATION = 'private'
        PRIVATE_FILE_STORAGE = f'{PROJECT_MAIN_APP_NAME}.storage_backends.PrivateMediaStorage'
    else:
        STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
        STATIC_URL = '/static/'
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
        MEDIA_URL = '/mediafiles/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

