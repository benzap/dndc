''' Database layer for storing dndc data
'''
import os
import sqlite3 as sqlite


class SQLiteDatabase:
    def __init__(self, file_path):
        self.file_path = file_path
        self.bconnected = False
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite.connect(file_path)
        self.bconnected = True
        
    def close(self):
        self.connection.close()
        self.bconnected = False

    def __enter__(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, etype, evalue, etraceback):
        if isinstance(evalue, Exception):
            self.cursor.rollback()
            self.cursor = None
            raise evalue
        else:
            self.cursor.commit()
            self.cursor = None
            return True



