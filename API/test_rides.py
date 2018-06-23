"""
Test all methods dealing with ride endpoints
"""
from app import app
import unittest
import json

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.ride_one = {"driver" : "John Doe" , "start_loc" : "Nairobi" , "end_loc" : "Thika",
            "departure_time" : "1800HRS" , "date" : "13/6/2018" , "route" : "Thika Super Highway" , "cost" : "400"}
        self.ride_two = {"driver" : "Jane Doe" , "start_loc" : "Nairobi", "end_loc" : "Syokimau",
            "departure_time" : "0900HRS", "date" : "14/6/2018" , "route" : "Mombas Road" , "cost" : "200"}
        self.request = { "pickup_loc" : "Roysambu"}
    '''
    GIVEN a user
    WHEN they view rides
    THEN test that all rides are returned
    '''
    def test_rides(self):
        response = self.app.get('/api/v1/allRides')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
    
    '''
    GIVEN a user
    WHEN they want to request a ride
    THEN test that they can send a request
    '''
    def test_ride_request(self):
        response = self.app.get('/api/v1/allRides/1')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)