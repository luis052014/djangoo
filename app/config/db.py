import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



POSTGRESQL={
    'default':{
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':'db1',
        'USER':'postgres',
        'PASSWORD':'052014',
        'HOST':'localhost',
        'PORT':'5432'

    }
}