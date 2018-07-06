import os
import psycopg2
import config
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from werkzeug.security import generate_password_hash
# from schema import Userschema, rideschema, requestschema
def dbconn():
    dbe= config.Config.db
    conn=psycopg2.connect(dbname=dbe["DATABASE_NAME"], user=dbe["DATABASE_USER"],password=dbe["DATABASE_PASS"],host=dbe["DATABASE_HOST"])
    return conn    

class User():

    def __init__(self, fname=None, lname=None,email=None,password=None):
        if fname and lname and email and password:
            self.fname = fname
            self.lname = lname
            self.email = email
            self.password = generate_password_hash(password)
    
    def create_user(self):
        conn = dbconn()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (fname, lname, email, password) VALUES (%s, %s, %s, %s) RETURNING id",
                                    (self.fname, self.lname, self.email, self.password))
        id = cur.fetchone()[0]
        conn.commit()
        conn.close()
        return id
    
    def login(self, email, password):
        conn = dbconn()
        cur = conn.cursor()
        cur.execute("SELECT password FROM users WHERE email = %s", (email,))
        row = cur.fetchone()
        return row
        
            

class Ride():
    def __init__(self, user_id=None, start_loc=None, end_loc=None,departure_time=None, date=None, route=None, cost=None):
        self.user_id = user_id
        self.start_loc = start_loc
        self.end_loc = end_loc
        self.departure_time = departure_time
        self.date = date
        self.route = route
        self.cost = cost
    def create_ride(self):
        conn = dbconn()
        cur = conn.cursor()
        cur.execute("INSERT INTO rides (user_id, start_loc, end_loc, depature_time, date, route, cost) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                    (self.user_id, self.start_loc, self.end_loc, self.departure_time, self.date,self.route,self.cost))
        conn.commit()
        conn.close()
    
    @staticmethod
    def get_rides():
        conn = dbconn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM rides;")
        rows = cur.fetchall()

        rides = {}
        for row in rows:
            rides[row[0]] = {
                'user_id': row[1],
                'start_loc':row[2],
                'end_loc': row[3],
                'departure_time': row[4],
                'date': row[5],
                'route': row[6],
                'cost': row[7]
            }
        return rides
    
    @staticmethod
    def get_ride(ride_id):
        conn = dbconn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM rides WHERE id=%s", (ride_id,))
        row = cur.fetchone()

        rides = {}
        rides[row[0]] = {
            'user_id': row[1],
            'start_loc':row[2],
            'end_loc': row[3],
            'departure_time': row[4],
            'date': row[5],
            'route': row[6],
            'cost': row[7]
        }

        return rides


class Request:
        def __init__(self=None, ride_id =None,pickup_loc=None, user_id =None):
            self.ride_id = ride_id
            self.pickup_loc = pickup_loc
            self.user_id = user_id
        
        def created_req(self):
            conn = dbconn()
            cur = conn.cursor()
            cur.execute("INSERT INTO requests (ride_id, pickup_loc, user_id) VALUES (%s, %s, %s)",
                                        [self.ride_id, self.pickup_loc, self.user_id])
            conn.commit()
            conn.close()
    
        #@staticmethod
        def get_requests(self):
            
            conn = dbconn()
            cur = conn.cursor()
            email = get_jwt_identity()
            cur.execute("SELECT id FROM users WHERE email=%s", (email,))
            use_id = cur.fetchone()
            user_id = use_id[0]
            cur.execute("SELECT * FROM requests WHERE user_id = %s AND ride_id = %s",(user_id,self.ride_id,))
            rows = cur.fetchall()

            req = {}
            for row in rows:
                req[row[0]] = {
                    'ride_id': row[1],
                    'status':row[2],
                    'pickup_loc': row[3]
                }
            return req

        @staticmethod
        def requests_resp(respo, req_id):
            conn = dbconn()
            cur = conn.cursor()
            cur.execute("UPDATE requests SET status=%s WHERE id=%s RETURNING status",(respo, req_id))
            status = cur.fetchone()[0]
            conn.commit()
            conn.close()
            return status
            