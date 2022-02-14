import sqlite3
import random


class DatabaseManager:
    def __init__(self, path):
        self.dictionary = dict()
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        row = cur.fetchone()
        while row is not None:
            self.dictionary[row[0]] = []
            row = cur.fetchone()
        for key in self.dictionary:
            cur.execute("SELECT * FROM '" + key + "';")
            row = cur.fetchone()
            while row is not None:
                self.dictionary[key].append(row[1])
                row = cur.fetchone()
        cur.close()
        conn.close()
