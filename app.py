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


if __name__ == '__main__':

    app.run(debug=True)