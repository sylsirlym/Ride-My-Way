import os
import sys
from os import environ
from flask import Flask,jsonify,request, make_response, abort
import json
import psycopg2
from models import User

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

@app.route('/')
def hello_world():
    "Hello. Welcome to Ride-My-Way. Nice to see you"
    return "Check out my docs: https://ridemyway-api.herokuapp.com/"

if __name__ == '__main__':
    # connectDB()
    app.run(debug=True)