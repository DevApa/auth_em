import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_mies',
        'USER': 'dbamies',
        'PASSWORD': 'M13$_2021',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_mies',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'OPTIONS': {
        'init_command': 'SET default_storage_engine=INNODB'
        # 'init_command': "SET sql_mode='STRICT_TRANS_TABLES",
        # 'init_command': "SET sql_mode='STRICT_ALL_TABLES'",
    }
}

ORACLE = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'entrepreneur',
        'USER': 'admin2021',
        'PASSWORD': 'Admin2021**',
        'HOST': 'localhost',
        'PORT': '1540',
    }
}
