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
        self.data = {"fname":"John", "lname":"Doe", "email":"mail@gmail.com","password":"pass123"}
        
    
    def test_register(self):
        """
        GIVEN a new user
        WHEN the user enters registration details
        THEN it checks the deatails
        """
        response = self.app.post('/api/v1/users/register', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["fname"], "John")
        self.assertEqual(result["lname"], "Doe")
        self.assertEqual(result["email"], "mail@gmail.com")
        self.assertEqual(result["password"], "pass123")
        self.assertEqual(response.status_code, 201)
    "//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
    
    def test_login(self):
        """
        GIVEN a  user
        WHEN the user enters authentication details
        THEN it checks the details and authenticates
        """
        response = self.app.get('/api/v1/users/login', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["email"], "mail@gmail.com")
        self.assertEqual(result["password"], "pass123")
        self.assertEqual(result["msg"], "You are logged in.Nice to see you again.")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()