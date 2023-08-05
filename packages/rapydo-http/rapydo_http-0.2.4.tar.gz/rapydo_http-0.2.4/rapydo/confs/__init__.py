# -*- coding: utf-8 -*-

# FIXME: move this inside the rapydo/__init__.py ?

import os

AVOID_COLORS_ENV_LABEL = 'TESTING_FLASK'
STACKTRACE = False
REMOVE_DATA_AT_INIT_TIME = False
#################################
# ENDPOINTS bases
API_URL = '/api'
AUTH_URL = '/auth'
STATIC_URL = '/static'
BASE_URLS = [API_URL, AUTH_URL]
#################################
# Directories for core code or user custom code
BACKEND_PACKAGE = 'rapydo'
# FIXME: all environment variables should be parameters in config YAML files
# only this would allow to have a running rapydo outside of docker
CUSTOM_PACKAGE = os.environ.get('VANILLA_PACKAGE', 'custom')
CORE_CONFIG_PATH = os.path.join(BACKEND_PACKAGE, 'confs')
# PROJECT_CONF_FILE = 'project_configuration'
# BLUEPRINT_KEY = 'blueprint'
#################################
# THE APP
DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = '5000'
USER_HOME = os.environ['HOME']
UPLOAD_FOLDER = '/uploads'
SECRET_KEY_FILE = os.environ.get('JWT_APP_SECRETS') + "/secret.key"

#################################
PRODUCTION = False
# DEBUG = False
if os.environ.get('APP_MODE', '') == 'production':
    PRODUCTION = True
# elif os.environ.get('APP_MODE', '') == 'debug':
#     DEBUG = True

#################################
# SQLALCHEMY
BASE_DB_DIR = '/dbs'
SQLLITE_EXTENSION = 'db'
SQLLITE_DBFILE = 'backend' + '.' + SQLLITE_EXTENSION
dbfile = os.path.join(BASE_DB_DIR, SQLLITE_DBFILE)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + dbfile
