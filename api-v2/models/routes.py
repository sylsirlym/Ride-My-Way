import os
import sys
from os import environ
from flask import Flask,jsonify,request, make_response, abort
import json
import psycopg2
from models import User,Ride

app = Flask (__name__)

@app.route('/api/v1/auth/register', methods = ['POST'])
def create_user():
    data = request.get_json()
    fname = data.get('fname')
    lname = data.get('lname')
    email = data.get('email')
    password = data.get('password')
    cpass = data.get('cpass')
    if fname is not None and lname is not None and email is not None and password is not None and cpass is not None: #Check deatils
        if cpass == password:
            User(fname=fname, lname=lname, email=email, password=password)
            return jsonify({
                    "message" : "Welcome to Ride-My-Way"}), 201
        else:
            return jsonify({
                "message" : "Please match your password"}), 201
    else:
        return jsonify({
                "message" : "Please make sure all fileds are filled"}), 201

@app.route('/api/v1/rides',  methods = ['POST'])
def create_ride():
    data = request.get_json()
    user_id = data.get('user_id')
    start_loc = data.get('start_loc')
    end_loc = data.get('end_loc')
    departure_time = data.get('departure_time')
    date = data.get('date')
    route = data.get('route')
    cost = data.get('cost')  

    if user_id is not None and start_loc is not None and end_loc is not None and departure_time is not None and date is not None and route is not None and cost is not None:

        Ride( 
            user_id = user_id, 
            start_loc = start_loc , 
            end_loc = end_loc,  
            departure_time=departure_time,
            date = date, 
            route = route,
            cost = cost  
            )
        return jsonify({
                "message" : "Succesfully created"}), 201

    else:
        return jsonify({
                "message" : "Please fill in all the fields"}), 201

# @app.route('/api/v1/rides')
# def get_rides():
#     ryde = 
#     rides =  ryde.get_all()

#     return jsonify({'rides': rides})

@app.route('/')
def hello_world():
    "Hello. Welcome to Ride-My-Way. Nice to see you"
    return "Check out my docs: https://ridemyway-api.herokuapp.com/"

if __name__ == '__main__':
    # connectDB()
    app.run(debug=True)