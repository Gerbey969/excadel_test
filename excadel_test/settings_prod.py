DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'excadel',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}
