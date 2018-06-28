"""Test all methods dealing with user endpoints
"""
import unittest
import json
import os

import sys  # fix import errors
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.ride_one = {"driver" : "John Doe" , "start_loc" : "Nairobi" , "end_loc" : "Thika",
            "departure_time" : "1800HRS" , "date" : "13/6/2018" , "route" : "Thika Super Highway" , "cost" : "400"}
        self.ride_two = {"driver" : "Jane Doe" , "start_loc" : "Nairobi", "end_loc" : "Syokimau",
            "departure_time" : "0900HRS", "date" : "14/6/2018" , "route" : "Mombas Road" , "cost" : "200"}
        self.request = { "pickup_loc" : "Roysambu"}
        self.ride_resp = { "respo" : "Accepted"}
    "//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
    def test_rides(self):
        '''
        GIVEN a user
        WHEN they view rides
        THEN test that all rides are returned
        '''
        response = self.app.get('/api/v1/rides', data = json.dumps(self.ride_two) , content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
    "////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
    def test_ride(self):
        '''
        GIVEN a user
        WHEN they view a single ride
        THEN test that the ride is returned
        '''
        response = self.app.get('/api/v1/rides/1', data = json.dumps(self.ride_two) , content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
    
    "///////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
    def test_ride_request(self):
        '''
        GIVEN a user
        WHEN they want to request a ride
        THEN test that they can send a request
        '''
        response = self.app.post('/api/v1/rides/1/requests', data = json.dumps(self.request) , content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_all_requests(self):
        '''
        GIVEN a user offers a ride
        WHEN they want to view request to the ride
        THEN test that they can send view request
        '''
        response = self.app.get('/api/v1/rides/1/requests', data = json.dumps(self.request) , content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_ride_respo(self):
        '''
        GIVEN a user
        WHEN they want to respond to a ride request
        THEN test that they can send a response
        '''
        response = self.app.put('/api/v1/rides/1/requests/1', data = json.dumps(self.ride_resp) , content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
    
    