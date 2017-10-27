import os

import environ


env = environ.Env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = env.str('SECRET_KEY', default='8b29aqm-g)9(%tp^)*f&$$u-9ndk11@n3wz2^2v%yz%1ndl(sd')

DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'CacheDemo'
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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

# Database configuration
DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres:///cachedemo')
}

DATABASES['default']['ATOMIC_REQUESTS'] = True

# Cache configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 60
    },
    'memcache': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
        'TIMEOUT': 60
    },
    'dummy': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
    'db': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'TIMEOUT': 10,
        'LOCATION': 'my_cache_table'
    },
    'filesystem': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/home/ivo/Code/blog/cache_for_speed_with_django/demo/CacheDemo/',
    },
    'redis': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': '{0}/{1}'.format(env('REDIS_URL', default='redis://127.0.0.1:6379'), 0),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,  # mimics memcache behavior.
                                        # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
        }
    },
    'redis_cache': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '{0}/{1}'.format(env('REDIS_URL', default='redis://127.0.0.1:6379'), 0),
    },

}
