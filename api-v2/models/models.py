import os
import psycopg2
import config
from werkzeug.security import generate_password_hash, check_password_hash

class Database:
    def __init__(self, app=None):
        dbe= config.Config.db
        self.conn=psycopg2.connect(dbname=dbe["DATABASE_NAME"], user=dbe["DATABASE_USER"],password=dbe["DATABASE_PASS"],host=dbe["DATABASE_HOST"])        
        self.cur = self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def cursor(self):
        return self.cur
    

database = Database()

class User(Database):

    def __init__(self, fname, lname,email,password):
        super().__init__()
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
    
    def create_user(self):
        cursor = database.cursor()
        cursor.execute("INSERT INTO users (fname, lname, email, password) VALUES (%s, %s, %s, %s)",
                                    (self.fname, self.lname, self.email, self.password))
        database.commit()
