"""
This gives the interactive documentation to help in getting started using the API
"""
import os

from flasgger import Swagger

import sys  # fix import errors
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

swagger = Swagger(app)

# Users
@app.route('/api/v1/users', methods=["POST"])
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


@app.route("/api/v1/users/<int:user_id>", methods=["GET"])
def get_single_user():
    """Getting single user endpoint
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/users/<int:user_id>', methods=["PUT"])
def update_user():
    """ Update a user endpoint
    parameters:
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
      - name: id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/users/<int:user_id>', methods=["DELETE"])
def delete_user():
    """ 
    Deleting an existing user endpoint.
    ---
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
    """


# Ride
@app.route('/api/v1/rides', methods=["POST"])
def create_ride():
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

@app.route("/api/v1/rides", methods=["GET"])
def get_all_rides():
    """Fetching all rides endpoint
    """

@app.route("/api/v1/rides/<int:ride_id>", methods=["GET"])
def get_one_ride():
    """Getting a specific ride endpoint.
    ---
    parameters:
      - name: ride_id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/rides/<int:ride_id>', methods=["PUT"])
def update_ride():
    """ endpoint for updating an existing ride.
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

@app.route('/api/v1/rides/<int:ride_id>', methods=["DELETE"])
def delete_ride():
    """ eDeleting n existing ride endpoint.
    ---
    parameters:
      - name: ride_id
        in: path
        type: integer
        required: true
    """


# request
@app.route('/api/v1/requestride/<int:ride_id>', methods=["POST"])
def request_ride():
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

@app.route("/api/v1/requests", methods=["GET"])
def get_all_requests():
    """View all requests endpoint
    """

@app.route("/api/v1/requests/<int:request_id>", methods=["GET"])
def get_one_request():
    """View a specific request endpoint
    ---
    parameters:
      - name: request_id
        in: path
        type: integer
        required: true
    """

@app.route('/api/v1/requests/<int:request_id>', methods=["PUT"])
def update_request():
    """ Update a request endpoint
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

app.route('/api/v1/requested/<int:request_id>', methods=["PUT"])
def update_request():
    """ respond a request endpoint
    ---
    parameters
      - name: request_id
        required: true
        in: path
        type: string
        """
@app.route('/api/v1/requests/<int:request_id>', methods=["DELETE"])
def delete_request():
    """ Delete a request endpoint
    ---
    parameters:
      - name: request_id
        in: path
        type: integer
        required: true
    """

@app.route('/')
def hello_world():
    "Hello. Welcome to Ride-My-Way. Nice to see you"
    return "Check out my docs: https://ridemyway-api.herokuapp.com/"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
app.run('0.0.0.0', port=port)