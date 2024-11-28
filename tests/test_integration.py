import unittest
from app import app

class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Set up a test client
        self.client = app.test_client()
        self.client.testing = True

    def test_hello_world_endpoint(self):
        # Send a GET request to the "/" route
        response = self.client.get("/")
        # Check the status code and response data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
