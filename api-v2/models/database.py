from os import environ
from flask import Flask
from psycopg2 import connect 
from psycopg2.extras import RealDictCursor #Access DB fields access columns only from keys
app = Flask (__name__)

app.config['CONN_STRING'] = environ.get('DB_CONN_STRING')
conn_string = app.config['CONN_STRING']

class Database(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
    def init_app(self, app):
        self.conn = connect(conn_string)
        #Return a cursor object, used to perform queries, assign the object to cur
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def query(self, query):
        self.cur.execute(query)

    def close(self):
        self.cur.close()
        self.conn.close()
