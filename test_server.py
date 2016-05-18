import unittest
from flask.ext.testing import TestCase
import server
import mock


class TestViews(TestCase):
    def create_app(self):
        app = server.app
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        return app

    def test_get(self):
        response = self.client.get("/")
        self.assertEqual(response.data, b'Not much to see here')

    @mock.patch('telegram.Bot')
    def test_empty_post(self, mock):
        _str_request = '{"message": {"message_id": 12, "text": "aj", "from": {"last_name": "Krivich", "username": "Kiote", "id": 124557099, "first_name": "Ekaterina"}, "chat": {"last_name": "Krivich", "username": "Kiote", "id": 124557099, "type": "private", "first_name": "Ekaterina"}, "date": 1462140570}, "update_id": 627598290}'
        response = self.client.post("/", data=_str_request, content_type='application/json')
        self.assertEqual(response.data, b'Hi, Kiote!')

    @mock.patch('telegram.Bot')
    def test_new_type(self, mock):
        _str_request = '{"message": {"message_id": 12, "text": "add new type", "from": {"last_name": "Krivich", "username": "Kiote", "id": 124557099, "first_name": "Ekaterina"}, "chat": {"last_name": "Krivich", "username": "Kiote", "id": 124557099, "type": "private", "first_name": "Ekaterina"}, "date": 1462140570}, "update_id": 627598290}'
        response = self.client.post("/", data=_str_request, content_type='application/json')
        self.assertEqual(response.data, b'Done, new type had been added.')

if __name__ == '__main__':
    unittest.main()
