'''Test cases for dndc.environment'''
import os
import os.path as path

import unittest

import dndc.environment as environment


TEST_DIR = path.dirname(path.abspath(__file__))


class TestCase_Environment(unittest.TestCase):
    def test_config_directory(self):
        if environment.ENV_CONFIG in os.environ:
            del os.environ[environment.ENV_CONFIG]

        self.assertEqual(environment.get_config_directory(),
                         environment.DEFAULT_CONFIG_DIRECTORY)

        os.environ[environment.ENV_CONFIG] = TEST_DIR

        self.assertEqual(environment.get_config_directory(),
                         TEST_DIR)
        
        del os.environ[environment.ENV_CONFIG]

    def test_data_directory(self):
        if environment.ENV_DATA in os.environ:
            del os.environ[environment.ENV_DATA]

        self.assertEqual(environment.get_data_directory(),
                         environment.DEFAULT_DATA_DIRECTORY)

        os.environ[environment.ENV_DATA] = TEST_DIR

        self.assertEqual(environment.get_data_directory(),
                         TEST_DIR)

        del os.environ[environment.ENV_DATA]

    def test_database_path(self):
        if environment.ENV_DB in os.environ:
            del os.environ[environment.ENV_DB]
        
        self.assertEqual(environment.get_database_path(),
                         path.join(environment.get_data_directory(), environment.DEFAULT_DATABASE))
