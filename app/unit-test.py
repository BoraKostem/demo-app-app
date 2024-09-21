import unittest
from demo_app import app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()