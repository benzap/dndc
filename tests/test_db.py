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
        self.database = db.SQLiteDatabase(DB_NAME).connect()

    def tearDown(self):
        self.database.close()
        self.database = None

    def test_database_connection(self):
        self.assertTrue(self.database.bconnected)
        self.assertTrue(self.database.connection is not None)
        
        self.database.close()
        self.assertFalse(self.database.bconnected)
        self.assertTrue(self.database.connection is None)

    def test_with_statement(self):
        with self.database as cursor:
            cursor.execute("CREATE TABLE test (id INTEGER PRIMARY KEY)")

    def test_insert_1(self):
        with self.database as cursor:
            cursor.execute(
            """
            CREATE TABLE test (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
            """)

            numrows = cursor.execute("""
            INSERT INTO test (name) VALUES ("test1")
            """)

            self.assertEqual(numrows, 1)

    def test_insert_with_query(self):
        with self.database as cursor:
            cursor.execute(
            """
            CREATE TABLE test (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
            """)

            numrows = cursor.execute("""
            INSERT INTO test (name) VALUES ("test1")
            """)

        with self.database as cursor:
            test_values = list(cursor.query("""SELECT * FROM test"""))

            self.assertEqual(len(test_values), 1)
            self.assertTrue(isinstance(test_values[0], dict))
            self.assertTrue("name" in test_values[0])

        with self.database as cursor:
            test_value = cursor.query_one("SELECT * FROM test")
            self.assertTrue("name" in test_value)
            self.assertEqual("test1", test_value["name"])

        with self.database as cursor:
            returned_id = cursor.execute_id("INSERT INTO test (name) VALUES ('test2')")
            self.assertTrue(isinstance(returned_id, int))
            self.assertTrue(returned_id > 0)

    def test_multiple_connections(self):
        with self.database as cursor1, self.database as cursor2:
            cursor1.execute(
            """
            CREATE TABLE test (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
            """)

            cursor2.execute(
            """
            CREATE TABLE test2 (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
            """)
        self.assertTrue(self.database.has_table("test"))
        self.assertIn("test", self.database.list_tables())
        self.assertIn("test2", self.database.list_tables())
