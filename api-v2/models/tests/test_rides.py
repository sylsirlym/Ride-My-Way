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

    def test_create_ride(self):

        response = self.app.post('/api/v1/rides', data = json.dumps(self.sample_ride), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        
if __name__ == '__main__':
    unittest.main()