from os import environ
from flask import Flask
import config
import psycopg2
from psycopg2.extras import RealDictCursor #Access DB fields access columns only from keys
app = Flask (__name__)

class Database:
    def __init__(self, app=None):
        dbe= config.Config.db
        self.conn=psycopg2.connect(dbname=dbe["DATABASE_NAME"], user=dbe["DATABASE_USER"],password=dbe["DATABASE_PASS"],host=dbe["DATABASE_HOST"])        
        self.cur = self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def cursor(self):
        return self.cur