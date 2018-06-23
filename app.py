import os

from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
import json 

app = Flask (__name__)


@app.route('/api/v1/register',  methods = ['POST'])
def register():
    data = request.get_json()
    fname = data['fname']
    lname = data['lname']
    email = data['email']
    password = data['password']
    return make_response(jsonify({
                                 "status": "ok",
                                 "fname": fname ,
                                 "lname": lname , 
                                 "email": email, 
                                 "password": password
                                 }), 201)
  
@app.route('/api/v1/login' , methods=['GET', 'POST'])
def login():
    return make_response(jsonify({
                                 "status": "ok",
                                 "msg": "You are logged in.Nice to see you again." 
                                 }), 200)

@app.route('/api/v1/allRides', methods=['GET'])
def allRides():
    return make_response(jsonify({
                                 "status": "ok",
                                 }), 200)

@app.route('/api/v1/rides',  methods = ['POST'])
def create_ride():
    data = request.get_json()
    driver = data['driver']
    start_loc = data['start_loc']
    end_loc = data['end_loc']
    departure_time = data['departure_time']
    date = data['date']
    route = data['route']
    cost = data['cost']
    return make_response(jsonify({
                                 "status": "ok",
                                 "driver": driver ,
                                 "start_loc": start_loc , 
                                 "end_loc": end_loc, 
                                 "departure_time": departure_time,
                                 "date": date, 
                                 "route": route, 
                                 "cost": cost
                                 }), 201)

if __name__ == '__main__':

    app.run(debug=True)