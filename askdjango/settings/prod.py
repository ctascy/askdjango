import os
from .common import *

DEBUG = False
ALLOWED_HOSTS =['*'] #별로 필요 없는 설정이라 모든 도메인에 대해 하겠다 common에는 빈리스트
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY)
STATIC_ROOT = os.path.join(BASE_DIR,'..','staticfiles')
DATABASES = {
    'default' :{
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'ubuntu',
        'USER' : 'ubuntu',
        'PASSWORD' : 'withaskdjango!',
        'HOST' : '127.0.0.1',
    }
}
