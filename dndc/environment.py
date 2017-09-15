''' Manages the location of where resources are stored and retrieved
'''
import os
import os.path as path

import dndc.db as db


ENV_CONFIG = "DNDC_CONFIG_DIRECTORY"
DEFAULT_CONFIG_DIRECTORY = path.expanduser("~/.dndc/config")
def get_config_directory():
    if ENV_CONFIG in os.environ:
        return os.environ[ENV_CONFIG]
    else:
        return DEFAULT_CONFIG_DIRECTORY


ENV_DATA = "DNDC_DATA_DIRECTORY"
DEFAULT_DATA_DIRECTORY = path.expanduser("~/.dndc/data")
def get_data_directory():
    if ENV_DATA in os.environ:
        return os.environ[ENV_DATA]
    else:
        return DEFAULT_DATA_DIRECTORY


ENV_DB = "DNDC_DATABASE"
DEFAULT_DATABASE = "default_database.dndc"
def get_database_path():
    db_name = DEFAULT_DATABASE
    if ENV_DB in os.environ:
        db_name = os.environ[ENV_DB]
    
    return path.join(get_data_directory(), db_name)


def get_db():
    return db.SQLiteDatabase(get_database_path())
