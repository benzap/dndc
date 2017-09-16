''' Database layer for storing dndc data
'''
import os

import sqlite3 as sqlite
import funcy as f

from dndc.utils import *


def execute_cursor(cursor, s, *args, **kwargs):
    if args:
        cursor.execute(s, args)
    elif kwargs:
        cursor.execute(s, kwargs)
    else:
        cursor.execute(s)    
        

def generate_rowmap(cursor, row):
    if row is None: return None

    column_names = (d[0] for d in cursor.description)
    row = dict(zip(column_names, row))
    return row


class Cursor:
    def __init__(self, cursor):
        self.cursor = cursor

    def execute(self, s, *args, **kwargs):
        execute_cursor(self.cursor, s, *args, **kwargs)
        return self.cursor.rowcount

    def query(self, s, *args, **kwargs):
        execute_cursor(self.cursor, s, *args, **kwargs)
        rows = self.cursor.fetchall()
        qrows = (generate_rowmap(self.cursor, row) for row in rows)
        return qrows

    def query_one(self, s, *args, **kwargs):
        execute_cursor(self.cursor, s, *args, **kwargs)
        row = self.cursor.fetchone()
        return generate_rowmap(self.cursor, row)

    def execute_id(self, s, *args, **kwargs):
        execute_cursor(self.cursor, s, *args, **kwargs)
        return self.cursor.lastrowid


class SQLiteDatabase:
    def __init__(self, file_path):
        self.file_path: str = file_path
        self.bconnected: bool = False
        self.connection = None
        self.cursor = None

    def connect(self):
        if self.connection is not None:
            self.connection.close()
        self.connection = sqlite.connect(self.file_path)
        self.bconnected = True
        return self
        
    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
        self.bconnected = False
        return self

    def __enter__(self):
        if self.connection is not None and self.bconnected:
            self.cursor = Cursor(self.connection.cursor())
        else:
            raise Exception("No connection has been made to the server")
        
        return self.cursor

    def __exit__(self, etype, evalue, etraceback):
        if isinstance(evalue, Exception):
            self.connection.rollback()
            self.cursor = None
            raise evalue
        else:
            self.connection.commit()
            self.cursor = None
            return True

    def has_table(self, name):
        with self as cursor:
            val = cursor.query_one("""
                                   SELECT name 
                                   FROM sqlite_master
                                   WHERE type = 'table'
                                   AND name = :name
                                   """, name=name)
            if val and val["name"] == name:
                return True
            return False

    def list_tables(self):
        with self as cursor:
            result = cursor.query("SELECT name FROM sqlite_master WHERE type='table'")
            return [row["name"] for row in result]

    def execute(self, s, *args, **kwargs):
        with self as cursor:
            return cursor.execute(s, *args, **kwargs)

    def execute_id(self, s, *args, **kwargs):
        with self as cursor:
            return cursor.execute_id(s, *args, **kwargs)

    def query(self, s, *args, **kwargs):
        with self as cursor:
            return cursor.query(s, *args, **kwargs)
        
    def query_one(self, s, *args, **kwargs):
        with self as cursor:
            return cursor.query_one(s, *args, **kwargs)

def main():
    import sys
    argv = sys.argv[1:]
    if len(argv) < 1:
        print("dndc-db <query> [args...]")
        sys.exit(0)

    from dndc.environment import get_db
    from pprint import pprint
    database = get_db()
    with database as cursor:
        rows = list(cursor.query(argv[0], *argv[1:]))
        pprint(rows)
        sys.exit(0)    

if __name__ ==  "__main__":
    main()
