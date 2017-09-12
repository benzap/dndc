''' Database layer for storing dndc data
'''
import os
import sqlite3 as sqlite


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
            self.cursor = self.connection.cursor()
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



