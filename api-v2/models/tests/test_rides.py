"""Test all methods dealing with user endpoints
"""
import os
import sys  # fix import errors
import unittest
import json
print(sys.path)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from routes import app

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
        
        self.sample_no_driver = {
            "start_loc" : "Nairobi" , 
            "end_loc" : "Thika",
            "departure_time" : "1800HRS" , 
            "date" : "13/6/2018" , 
            "route" : "Thika Super Highway" , 
            "cost" : "400"
            }
        
        self.sample_no_start = {
            "driver" : "Jane Dore" , 
            "end_loc" : "Thika",
            "departure_time" : "1800HRS" , 
            "date" : "13/6/2018" , 
            "route" : "Thika Super Highway" , 
            "cost" : "400"
            }
        self.sample_req = {
            "pickup_loc":"Roy"
        }
        self.sample_requ = {
            "pickup":"Roy"
        }

    def test_create_ride(self):
        """
        GIVEN a  user
        WHEN the user tries to create a ride without uthentication
        THEN it checks the details and returns a unauthorized
        """
        response = self.app.post(
            '/api/v1/users/rides', 
            data = json.dumps(self.sample_ride), 
            content_type = 'application/json')
        self.assertEqual(response.status_code, 401)
    
    def test_no_driver_create_ride(self):
        """
        GIVEN a  user
        WHEN the user tries to create a ride without uthentication
        THEN it checks the details and returns a unauthorized
        """
        response = self.app.post(
            '/api/v1/users/rides', 
            data = json.dumps(self.sample_no_driver), 
            content_type = 'application/json')
        self.assertEqual(response.status_code, 401)
    
    def test_no_driver_start_loc(self):
        """
        GIVEN a  user
        WHEN the user tries to create a ride without uthentication
        THEN it checks the details and returns a unauthorized
        """
        response = self.app.post(
            '/api/v1/users/rides', 
            data = json.dumps(self.sample_no_start), 
            content_type = 'application/json')
        self.assertEqual(response.status_code, 401)
    
    def test_create_request(self):
        """
        GIVEN a  user
        WHEN the user tries to create a request without uthentication
        THEN it checks the details and returns a unauthorized
        """
        response = self.app.post(
            '/api/v1/rides/1/requests', 
            data = json.dumps(self.sample_req), 
            content_type = 'application/json')
        self.assertEqual(response.status_code, 401)
    
    def test_pickup_loc(self):
        """
        GIVEN a  user
        WHEN the user tries to create a request without uthentication
        THEN it checks the details and returns a unauthorized
        """
        response = self.app.post(
            '/api/v1/rides/1/requests', 
            data = json.dumps(self.sample_requ), 
            content_type = 'application/json')
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()