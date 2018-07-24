import os
import sys
from os import environ
from flask import Flask,jsonify,request, make_response, abort
from werkzeug.security import check_password_hash
import json
import psycopg2
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import User,Ride,Request, dbconn
from marshmallow import Schema, fields
from schema import Userschema, rideschema, requestschema, responsechema

app = Flask (__name__)

app.config['JWT_SECRET_KEY'] = 'secrets'
JWT_MANAGER=JWTManager()
JWT_MANAGER.init_app(app)

@app.route('/api/v1/auth/register', methods = ['POST'])
def create_user():
    in_data = request.get_json()
    data = Userschema.load(in_data)
    # import pdb; pdb.set_trace()
    # if errors:
    #     return (errors), 400
    fname = data.get('fname')
    lname = data.get('lname')
    email = data.get('email')
    password = data.get('password')
    cpass = data.get('cpass')
    if fname is not None and lname is not None and email is not None and password is not None and cpass is not None: #Check deatils
        if cpass == password:
            new_user=User(fname=fname, lname=lname, email=email, password=password)
            new_user.create_user()
            return jsonify({
                    "message" : "Welcome to Ride-My-Way"
                    }), 201
        else:
            return jsonify({
                "message" : "Please match your password"}), 401
    else:
        return jsonify({
                "message" : "Please make sure all fileds are filled"}), 400

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if email is not None and password is not None:
        user = User()
        log = user.login(email, password)
        if log is not None:
            if check_password_hash(log[0], password): 
                access_token = create_access_token(identity=email)
                return jsonify({
                        "message" : "Welcome to Ride-My-Way",
                        "token" : access_token,
                        }), 200
            else:
                return jsonify({
                        "message" : "Input the correct password",
                        }), 401
        else:
            return jsonify({"message":"Please register"}), 404

#Rides  
@app.route('/api/v1/users/rides',  methods = ['POST'])
@jwt_required
def create_ride():
    conn = dbconn()
    cur = conn.cursor()
    email = get_jwt_identity()
    cur.execute("SELECT id FROM users WHERE email=%s", (email,))
    user_id = cur.fetchone()
    in_data = request.get_json()
    data = rideschema.load(in_data)
    start_loc = data.get('start_loc')
    end_loc = data.get('end_loc')
    departure_time = data.get('departure_time')
    date = data.get('date')
    route = data.get('route')
    cost = data.get('cost')  

    if user_id is not None and start_loc is not None and end_loc is not None and departure_time is not None and date is not None and route is not None and cost is not None:

        new_ride= Ride( 
            user_id = user_id, 
            start_loc = start_loc , 
            end_loc = end_loc,  
            departure_time=departure_time,
            date = date, 
            route = route,
            cost = cost  
            )
        new_ride.create_ride()
        return jsonify({
                "message" : "Succesfully created"}), 201

    else:
        return jsonify({
                "message" : "Please fill in all the fields"}), 400

@app.route('/api/v1/rides', methods = ['GET'])
def get_rides():

    rides = Ride.get_rides()
    return jsonify({'rides': rides})

@app.route('/api/v1/rides/<int:ride_id>', methods = ['GET'])
def get_ride(ride_id):

    rides = Ride.get_ride(ride_id)
    if len(rides) != 0:
        return jsonify({'rides': rides})
    return jsonify ({"message": "Ride not found"})

#Request
@app.route('/api/v1/rides/<int:ride_id>/requests',  methods = ['POST'])
@jwt_required
def create_request(ride_id):
    conn = dbconn()
    cur = conn.cursor()
    email = get_jwt_identity()
    cur.execute("SELECT id FROM users WHERE email=%s", (email,))
    user_id = cur.fetchone()
    in_data = request.get_json()
    data = requestschema.load(in_data)
    ride_id = ride_id,
    pickup_loc = data.get('pickup_loc'),
    #Check if ride is available, and select its creator
    cur.execute("SELECT user_id FROM rides WHERE id=%s", (ride_id,))
    u_id = cur.fetchone()
    if u_id is not None:
         
        if u_id != user_id:

            if pickup_loc is not None:

                new_req = Request(ride_id=ride_id, pickup_loc= pickup_loc, user_id=user_id)
                new_req.created_req()
                return (jsonify({
                        "message" : "Request successfully submitted"}), 201)
            else:
                return (jsonify({
                        "message" : "Please fill in all the fields"}), 400)
        else: return (jsonify({
                        "message": "You cannot request your own ride"}),400)
    else:
        return  (jsonify({
                "mesaage":"Ride is not found"}), 400)   

@app.route('/api/v1/rides/<int:ride_id>/requests', methods = ['GET'])
@jwt_required
def get_requests(ride_id):
    conn = dbconn()
    cur = conn.cursor()
    email = get_jwt_identity()
    cur.execute("SELECT id FROM users WHERE email=%s", (email,))
    user_id = cur.fetchone()
    cur.execute("SELECT id FROM rides WHERE user_id=%s", (user_id,))
    r_id = cur.fetchone()
    if r_id == ride_id:
        new_req = Request(ride_id=ride_id)
        requests = new_req.get_requests()
        return (jsonify({'requests': requests}), 200)
    else:
        return (jsonify({'message': "You cannot view request to this ride. It is not your ride"}), 400)


@app.route('/api/v1/rides/<int:ride_id>/requests/<int:req_id>', methods = ['PUT'])
@jwt_required
def request_respo(ride_id, req_id):
    conn = dbconn()
    cur = conn.cursor()
    email = get_jwt_identity()
    cur.execute("SELECT id FROM users WHERE email=%s", (email,))
    user_id = cur.fetchone()
    cur.execute("SELECT id FROM rides WHERE user_id=%s", (user_id,))
    r_id = cur.fetchone()
    if r_id == ride_id:
        in_data = request.get_json()
        data = requestschema.load(in_data)
        respo = data['status']

        if respo is not None:
            req_resp = Request()
            status = req_resp.requests_resp(respo, req_id)

        return jsonify({'msg': "Request has been " + status}, 200)
    else:
        return (jsonify({'message': "You cannot respond to requests made to this ride. It is not your ride"}), 400)
    

@app.route('/')
def hello_world():
    "Hello. Welcome to Ride-My-Way. Nice to see you"
    return "Check out my docs: https://ridemyway-api.herokuapp.com/"

if __name__ == '__main__':
    # connectDB()
    app.run(debug=True)