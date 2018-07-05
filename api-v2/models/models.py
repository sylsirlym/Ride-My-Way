import os
import psycopg2
import config
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash

def dbconn():
    dbe= config.Config.db
    conn=psycopg2.connect(dbname=dbe["DATABASE_NAME"], user=dbe["DATABASE_USER"],password=dbe["DATABASE_PASS"],host=dbe["DATABASE_HOST"])
    return conn    

class User():

    def __init__(self, fname, lname,email,password):
        super().__init__()
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
    
    def create_user(self):
        conn = dbconn()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (fname, lname, email, password) VALUES (%s, %s, %s, %s)",
                                    (self.fname, self.lname, self.email, self.password))
        conn.commit()
        conn.close()

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

        # if row is None:
        #     return jsonify({
        #         "message" : "Ride not found"}), 404

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


class Request():
        def __init__(self, ride_id =None,pickup_loc=None):
            self.ride_id = ride_id
            self.pickup_loc = pickup_loc
        def created_req(self):
            conn = dbconn()
            cur = conn.cursor()
            cur.execute("INSERT INTO requests (ride_id, pickup_loc) VALUES (%s, %s)",
                                        [self.ride_id, self.pickup_loc])
            conn.commit()
            conn.close()
    
        @staticmethod
        def get_requests():
            conn = dbconn()
            cur = conn.cursor()
            cur.execute("SELECT * FROM requests;")
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