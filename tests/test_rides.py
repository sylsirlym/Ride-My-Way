"""
Test all methods dealing with ride endpoints
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
        self.ride_one = {"id" : "1" , "driver" : "John Doe" , "start_loc" : "Nairobi" , "end_loc" : "Thika",
            "departure_time" : "1800HRS" , "date" : "13/6/2018" , "route" : "Thika Super Highway" , "cost" : "400"}
        self.ride_two = {"pickup_loc" : "Allsops"}
    
    def test_rides(self):
        response = self.app.get('/api/v1/rides')
        self.assertEqual(response.status_code, 200)

    '''
    GIVEN a user
    WHEN they want to request a ride
    THEN test that they can send a request
    '''
    def test_ride_request(self):
        response = self.app.post('/api/v1/ride/1' , data = json.dumps(self.ride_two) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["pickup_loc"], "Allsops")
        self.assertEqual(response.status_code, 201)

    """GIVEN a user
    WHEN the user wants to create a ride
    THEN it checks the details
    """
    def test_create_ride(self):
        response = self.app.post('/api/v1/rides', data = json.dumps(self.ride_one) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["driver"], "John" + " Doe")
        self.assertEqual(result["start_loc"], "Nairobi")
        self.assertEqual(result["end_loc"], "Thika")
        self.assertEqual(result["departure_time"], "1800HRS")
        self.assertEqual(result["date"], "13/6/2018")
        self.assertEqual(result["route"], "Thika Super Highway")
        self.assertEqual(result["cost"], "400")
        self.assertEqual(response.status_code, 201)
    
    def test_specific_ride(self):
        response = self.app.get('/api/v1/rides/1', data = json.dumps(self.ride_one) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["id"], "1")
        self.assertEqual(response.status_code, 200)