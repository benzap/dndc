'''Test cases for dndc.db
'''
import os
import os.path as path

import unittest

import dndc.db as db


TEST_DIR = path.dirname(path.abspath(__file__))
DB_NAME: str = path.join(TEST_DIR, "test_database.dndc")


class TestCase_Database(unittest.TestCase):
    def setUp(self):
        if path.exists(DB_NAME):
            print(f"Deleting {DB_NAME}...")
            os.remove(DB_NAME)

    def tearDown(self):
        pass

    def test_database_connection(self):
        database = db.SQLiteDatabase(DB_NAME).connect()
        self.assertTrue(database.bconnected)
        self.assertTrue(database.connection is not None)
        
        database.close()
        self.assertFalse(database.bconnected)
        self.assertTrue(database.connection is None)

    def test_with_statement(self):
        database = db.SQLiteDatabase(DB_NAME).connect()
        with database as cursor:
            cursor.execute("CREATE TABLE test (id INTEGER PRIMARY KEY)")
