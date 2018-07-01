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
        self.data = {
            "fname":"John", 
            "lname":"Doe", 
            "email":"mail@gmail.com",
            "password":"pass123"
            }
        
    
    def test_registration(self):
        """
        GIVEN a new user
        WHEN the user enters registration details
        THEN it checks the details
        """
        
        response = self.app.post(
            '/api/v1/auth/register', 
            data = json.dumps(self.data) , 
            content_type = 'application/json'
            )
        self.assertEqual(response.status_code, 200)

    def test_invalid_registration(self):
        """
        Given a user
        WHEN the user inputs 
        Test invalid method.
        """
        data = {
            'email':'mail@gmail.com',
            'password':'pass123',
            'lname':'Doe', 
            'fname':'Jon'
            
            }
        response = self.app.put(
            '/api/v1/auth/register', 
            data = json.dumps(data) , 
            content_type = 'application/json'
            )
        self.assertEqual(response.status_code, 405)


    
    def test_login(self):
        """
        GIVEN a  user
        WHEN the user enters authentication details
        THEN it checks the details and authenticates
        """
        response = self.app.get(
            '/api/v1/auth/login', 
            data = json.dumps(self.data) , 
            content_type = 'application/json'
            )
        self.assertEqual(response.status_code, 200)
    




if __name__ == '__main__':
    unittest.main()