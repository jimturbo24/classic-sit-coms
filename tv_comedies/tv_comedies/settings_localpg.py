from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tv_comedies_localdb',
        'USER': 'tv_comedies_user',
        'PASSWORD': 'tooEhee24',
        'HOST': '',
        'PORT': '',
    }
}
