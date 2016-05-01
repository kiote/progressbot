import unittest
from flask.ext.testing import TestCase
import server


class TestViews(TestCase):
    def create_app(self):
        app = server.app
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        return app

    def test_get(self):
        response = self.client.get("/")
        self.assertEquals(response.data, b'Not much to see here')

    def test_empty_post(self):
        response = self.client.post("/")
        self.assertEquals(response.data, b'hi')

if __name__ == '__main__':
    unittest.main()
