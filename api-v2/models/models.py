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

class User():

    def __init__(self, fname, lname,email,password):
        super().__init__()
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
    
    #def create_user(self):
        cursor = database.cursor()
        cursor.execute("INSERT INTO users (fname, lname, email, password) VALUES (%s, %s, %s, %s)",
                                    (self.fname, self.lname, self.email, self.password))
        database.commit()

class Ride():
    def __init__(self, user_id=None, start_loc=None, end_loc=None,departure_time=None, date=None, route=None, cost=None):
        self.user_id = user_id
        self.start_loc = start_loc
        self.end_loc = end_loc
        self.departure_time = departure_time
        self.date = date
        self.route = route
        self.cost = cost
    # def create_ride()
        cursor = database.cursor()
        cursor.execute("INSERT INTO rides (user_id, start_loc, end_loc, depature_time, date, route, cost) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                    (self.user_id, self.start_loc, self.end_loc, self.departure_time, self.date,self.route,self.cost))
        database.commit()

class Request():
        def __init__(self, ride_id =None,pickup_loc=None):
            self.ride_id = ride_id
            self.pickup_loc = pickup_loc
        def created_req(self):
            cursor = database.cursor()
            cursor.execute("INSERT INTO requests (ride_id, pickup_loc) VALUES (%s, %s)",
                                        (self.ride_id, self.pickup_loc))
            database.commit()