"""
This gives the interactive documentation to help in getting started using the API
"""
import os
from flask import Flask,jsonify,request, make_response
import json
import psycopg2

app = Flask (__name__)

def connectDB():
    
     #Define a connection string
    conn_string = "host='localhost' dbname='ridemyway' user='postgres' password='Secrets'"
     # Print the connection string we will use to connect
    
     # Initialize a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
 
	 # conn.cursor will return a cursor object, used to perform queries
    cursor = conn.cursor()
    print ("Connected!\n")
    conn.close()


rides = [
    {   'id' : 1 ,
        'driver' : 'John Doe' ,
        'start_loc' : 'Nairobi' , 
        'end_loc' : 'Thika',
        'departure_time' : '1800HRS' , 
        'date' : '13/6/2018' , 
        'route' : 'Thika Super Highway' , 
        'cost' : '400'
    } ,
    {   
        'id' : 2 ,
        'driver' : 'Jane Doe' , 
        'start_loc' : 'Nairobi', 
        'end_loc' : 'Syokimau',
        'departure_time' : '0900HRS', 
        'date' : '14/6/2018' , 
        'route' : 'Mombasa Road' , 
        'cost' : '200'
    }
]

ride_resp = [
    {   
        'req_id' : '1',
        'respo': 'Accepted'
    }
]

users =[
    {
        'fname':'John', 
        'lname':'Doe', 
        'email':'email@gmail.com',
        'password':'pass123'
    }
]



requested = [
    {   'id' : '1',
        'pickup_loc': 'Allsops'
    }
]

ride_response = [
    {   'ride_id' : '1',
        'respo': 'Accepted'
    }
]

dummy_user = {
        'fname':'John', 
        'lname':'Doe', 
        'email':'mail@gmail.com',
        'password':'pass123'
    }


# Users
@app.route('/api/v1/users/register', methods=["GET", "POST"])
def signup():
    """ 
    User registeration endpoint.
    ---
    parameters:
      - name: fname
        in: application/json
        type: string
        required: true
      - name: lname
        in: application/json
        type: string
        required: true
      - name: email
        in: application/json
        type: string
        required: true  
      - name: password
        in: application/json
        type: string
        required: true
      - name: conf_password
        in: application/json
        type: string
        required: true
    """
    if request.method == 'GET':
        return jsonify({'fields to fill': users})
    elif request.method == 'POST':
        new_user = {
            'fname': request.json['fname'],
            'lname': request.json['lname'],
            'email': request.json['email'],
            'password': request.json['password']
        }

    #add the new use to list of users
    users.append(new_user)
    return jsonify({'users': users})
"/////////////////////////////////////////////////////////////////////////////////////////"

@app.route('/api/v1/users/login', methods=['GET', 'POST'])
def login():
    known_user = {
        'email': '',
        'password': ''
    }
    if request.method=='GET':
        return jsonify({'Enter this':known_user})

    elif request.method == 'POST':
        known_user = {
            'email': request.json['email'],
            'password': request.json['password']
        }
        #loop through users to find user email and password
        #using password for authentication illustration
        for user in users:
            #check if the password got == password registered
            if user.get('password') == known_user.get('password'):
                return jsonify({'You are logged in.Nice to see you again.': known_user.get('email')})

        return jsonify({'Please register': known_user.get('email')})

"////////////////////////////////////////////////////////////////////////////////////////"
# Ride
@app.route('/api/v1/rides', methods=["POST"])
def new_ride():
    """ 
    Creating a ride endpoint
    ---
    parameters:
      - name: driver
        required: true
        in: application/json
        type: string
      - name: start_loc
        required: true
        in: application/json
        type: string
      - name: end_loc
        required: true
        in: application/json
        type: string
      - name: time
        in: application/json
        type: string
        required: true
      - name: date
        required: true
        in: application/json
        type: string
      - name: route
        required: true
        in: application/json
        type: string
      - name: cost
        required: true
        in: application/json
        type: string
    """
    new_ride = {
        'id': request.json['id'],
        'driver': request.json['driver'],
        "start_loc" : request.json['start_loc'], 
        "end_loc" : request.json['end_loc'],
        "departure_time" : request.json['departure_time'], 
        "date" : request.json['date'] , 
        "route" : request.json['route'] , 
        "cost" : request.json['cost']
    }

    """Append to the list holdng all ride details"""
    #Issue a bad request error
    rides.append(new_ride) #append new ride to the other rides
    return make_response(jsonify({'new_ride': new_ride}), 201)

"////////////////////////////////////////////////////////////////////////////////////////"
@app.route("/api/v1/rides", methods=["GET"])
def get_all_rides():
    """Fetching all rides endpoint
    """
    all_rides = {}
    for ride in rides:
        ride_id = ride.get('id')
        ride_title = ride.get('start_loc')+' - '+ ride.get('end_loc')
    
        #add the id and title to dictionary
        all_rides.update({ride_id : ride_title})
    return jsonify(all_rides)
"/////////////////////////////////////////////////////////////////////////////////////"
@app.route("/api/v1/rides/<int:id>", methods=["GET"])
def get_ride(id):
    
  #loop through the rides and find ride with the id
    for ride in rides:

      if ride.get('id') == id:
            #store the ride details in variable
            search = ride
            # return the data in json format
    return jsonify({'Ride': search})
"////////////////////////////////////////////////////////////////////////////////////////////"

@app.route('/api/v1/rides/<int:id>', methods=["GET", "PUT"])
def update_ride(id):
    """ endpoint for updating an existing ride.
    ---
    
      parameters:
      - name: ride_id
        in: path
        type: integer
        required: true
      - Create ride parameters
    """
    """Loop through all rides and find ride with entered id"""
    edit_details = {
          'id': request.json['id'],
          'driver': request.json['driver'],
          "start_loc" : request.json['start_loc'], 
          "end_loc" : request.json['end_loc'],
          "departure_time" : request.json['departure_time'], 
          "date" : request.json['date'] , 
          "route" : request.json['route'] , 
          "cost" : request.json['cost']
        }

    """Append to the list holdng all ride details"""
    rides.append(edit_details)

        #new dictionary to add id and title
    all_rides = {}
        #loop through the dictionary and find all ids and titles

    for ride in rides:
        ride_id = str(ride.get('id'))
        ride_title = ride.get('start_loc')+' - '+ ride.get('end_loc')

            #add the id and title to dictionary
        all_rides.update({ride_id: ride_title})
    return jsonify(all_rides)
"//////////////////////////////////////////////////////////////////////////////////////"

@app.route('/api/v1/rides/<int:id>', methods=["DELETE"])
def delete_ride(id):
    """ eDeleting n existing ride endpoint.
    ---
    parameters:
      - name: ride_id
        in: path
        type: integer
        required: true
    """
    #loop through rides ad find ride with id given
    for ride in rides:
        if ride.get('id')==id:
            to_delete = ride
            #find the index of the ride
            ride_index = rides.index(to_delete)

            #delete the ride entry
            ride_deleted = rides.pop(ride_index)

    return jsonify({'You deleted': ride_deleted})
"/////////////////////////////////////////////////////////////////////////////////////////////"
# request
@app.route('/api/v1/rides/<int:id>/requests', methods=["GET", "POST"])
def ride_request(id):
    """ Requesting ride endpoint.
    ---
    parameters:
      - name: ride_id
        required: true
        in: path
        type: string
      - name: pickup_loc
        required: true
        in: path
        type: string
    """
    if request.method=='GET':
        """Fetching all requested rides endpoint
        """
        return make_response(jsonify({'requested_rides': requested}), 200)
    elif request.method=='PUT':
        req = {
          'id' : id,
          'pickup_loc': request.json['pickup_loc'],
        }

        #loop through the dictionary and find all ids and titles
    requested.append(req) #append new ride to the other rides
    return make_response(jsonify({'request': req}), 201)

"/////////////////////////////////////////////////////////////////////////////////////"
@app.route('/api/v1/rides/<int:id>/requests/<int:req_id>', methods=["PUT"])
def respond(id,req_id):
    """ Responding to requested rides
    ---
    parameters:
      - name: request_id
        required: true
        in: path
        type: string
      - name: response
        required: true
        in: path
        type: string
    """
    respo = {
          'req_id' : req_id,
          'respo': request.json['respo'],
        }

        #loop through the dictionary and find all ids and titles
    ride_resp.append(respo) #append new ride to the other rides
    return make_response(jsonify({'respo': respo}), 200)

"/////////////////////////////////////////////////////////////////////////////"


@app.route('/')
def hello_world():
    "Hello. Welcome to Ride-My-Way. Nice to see you"
    return "Check out my docs: https://ridemyway-api.herokuapp.com/"


if __name__ == '__main__':
    connectDB()
    app.run(debug=True)
    