"""Test all methods dealing with user endpoints
"""
from app import app
import unittest
import json

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.data = {"fname":"John", "lname":"Doe", "email":"mail@gmail.com","password":"pass123"}
    """GIVEN a new user
   WHEN the user enters registration details
   THEN it checks the deatails
   """
    def test_register(self):
        response = self.app.post('/api/v1/register', data = json.dumps(self.data) , content_type = 'application/json')
        result = json.loads(response.data)
        self.assertEqual(result["fname"], "John")
        self.assertEqual(result["lname"], "Doe")
        self.assertEqual(result["email"], "mail@gmail.com")
        self.assertEqual(result["password"], "pass123")
        self.assertEqual(response.status_code, 201)
    """
    GIVEN a  user
    WHEN the user enters authentication details
    THEN it checks the details and authenticates
    """

    def test_login(self):
        response = self.app.get('/api/v1/login')
        result = json.loads(response.data)
        self.assertEqual(result["msg"], "You are logged in.Nice to see you again.")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()