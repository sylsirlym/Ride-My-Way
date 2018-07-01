"""Test all methods dealing with user endpoints
"""
import unittest
import json
import os

import sys  # fix import errors

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, rides


class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.sample_ride = {
            "driver" : "John Doe" , 
            "start_loc" : "Nairobi" , 
            "end_loc" : "Thika",
            "departure_time" : "1800HRS" , 
            "date" : "13/6/2018" , 
            "route" : "Thika Super Highway" , 
            "cost" : "400"
            }
        self.request = { 
            "pickup_loc" : "Roysambu"
            }
        self.ride_resp = { 
            "respo" : "Accepted"
            }

    def test_create_ride(self):
        response = self.app.post('/api/v1/rides', data = json.dumps(self.sample_ride), content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        """Test data match"""
        data = []
        data = result["new_ride"]
        assert data["driver"] == self.sample_ride["driver"]
        assert data["start_loc"] == self.sample_ride["start_loc"]
        assert data["end_loc"] == self.sample_ride["end_loc"]
        assert data["departure_time"] == self.sample_ride["departure_time"]
        assert data["date"] == self.sample_ride["date"]
        assert data["route"] == self.sample_ride["route"]
        assert data["cost"] == self.sample_ride["cost"]



    
    def test_rides(self):
        '''
        GIVEN a user
        WHEN they view rides
        THEN test that all rides are returned
        '''
        response = self.app.get('/api/v1/rides')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(rides), 2)



    def test_ride(self):
        '''
        GIVEN a user
        WHEN they view a single ride
        THEN test that the ride is returned
        '''
        response = self.app.get('/api/v1/rides/1')
        self.assertEqual(response.status_code, 200)
    

    def test_ride_request(self):
        '''
        GIVEN a user
        WHEN they want to request a ride
        THEN test that they can send a request
        '''
        response = self.app.post('/api/v1/rides/1/requests', data = json.dumps(self.request) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        data = []
        data = result["req"]
        assert data["pickup_loc"] == self.request["pickup_loc"]
    
    def test_all_requests(self):
        '''
        GIVEN a user offers a ride
        WHEN they want to view request to the ride
        THEN test that they can view request
        '''
        response = self.app.get('/api/v1/rides/1/requests', data = json.dumps(self.request) , content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
       
    
    def test_ride_respo(self):
        '''
        GIVEN a user
        WHEN they want to respond to a ride request
        THEN test that they can send a response
        '''
        response = self.app.post('/api/v1/rides/1/requests/1', data = json.dumps(self.ride_resp) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        data = []
        data = result["respo"]
        assert data["respo"] == self.ride_resp["respo"]
    
    
    
