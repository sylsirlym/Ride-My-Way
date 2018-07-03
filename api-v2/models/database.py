from psycopg2 import connect 
from psycopg2.extras import RealDictCursor #Access DB fields access columns only from keys

class Database(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
    
    def init_app(self, app):
        self.conn = connect("host='localhost' dbname='ridemyway' user='postgres' password='Secrets'")
        #Return a cursor object, used to perform queries, assign the object to cur
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def query(self, query):
        self.cur.execute(query)

    def close(self):
        self.cur.close()
        self.conn.close()