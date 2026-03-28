TIME_ZONE = 'America/Detroit'
LANGUAGE_CODE = 'en-us'
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}