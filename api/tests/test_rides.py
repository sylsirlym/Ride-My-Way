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
        self.ride_one = {"driver" : "John Doe" , "start_loc" : "Nairobi" , "end_loc" : "Thika",
            "departure_time" : "1800HRS" , "date" : "13/6/2018" , "route" : "Thika Super Highway" , "cost" : "400"}
        self.ride_two = {"driver" : "Jane Doe" , "start_loc" : "Nairobi", "end_loc" : "Syokimau",
            "departure_time" : "0900HRS", "date" : "14/6/2018" , "route" : "Mombas Road" , "cost" : "200"}
    
    def test_rides(self):
        response = self.app.get('/api/v1/allRides')
        self.assertEqual(response.status_code, 200)
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