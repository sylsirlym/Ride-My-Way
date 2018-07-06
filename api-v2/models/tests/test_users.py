"""Test all methods dealing with user endpoints
"""
import os
import sys  # fix import errors
import unittest
import json
import psycopg2
print(sys.path)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from routes import app

def dbconn():
    conn = psycopg2.connect("dbname='testdb' user='postgres' password='Secrets' host='localhost'")
    return conn
    cur = conn.cursor()

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {
            "fname":"John", 
            "lname":"Doe", 
            "email":"mail@gmail.com",
            "password":"pass123",
            "cpass" : "pass123"
            }
        self.fname_data = { 
            "lname":"Doe", 
            "email":"mail@gmail.com",
            "password":"pass123",
            "cpass" : "pass123"
            }
        self.lname_data = { 
            "fname":"Doe", 
            "email":"mail@gmail.com",
            "password":"pass123",
            "cpass" : "pass123"
            }
        self.faulty_data = {
            "fname":"John", 
            "lname":"Doe", 
            "email":"mail@gmail.com",
            "password":"pass123",
            "cpass" : "pass"
            }
        self.sample_login={
            "email":"mail1@gmail.com",
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
        self.assertEqual(response.status_code, 201)

    def test_invalid_registration(self):
        """
        Given a user
        WHEN the user inputs 
        Test invalid method.
        """
        response = self.app.post(
            '/api/v1/auth/register', 
            data = json.dumps(self.faulty_data) , 
            content_type = 'application/json'
            )
        self.assertEqual(response.status_code, 401)

    def test_fname_empty(self):
        response = self.app.post(
            '/api/v1/auth/register', 
            data = json.dumps(self.fname_data) , 
            content_type = 'application/json'
            )
        self.assertEqual(response.status_code, 400)

    def test_lname_empty(self):
        res = self.app.post(
        '/api/v1/auth/register', 
        data = json.dumps(self.lname_data) , 
        content_type = 'application/json'
        )
        self.assertEqual(res.status_code, 400)

    def test_login(self):
        """
        GIVEN a  user
        WHEN the user enters wrong authentication details
        THEN it checks the details and returns a bad request
        """
        response = self.app.post(
            '/api/v1/auth/login', 
            data = json.dumps(self.sample_login) , 
            content_type = 'application/json'
            )
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()