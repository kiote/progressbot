import unittest
import chat.config as config
import server
import mock

from flask.ext.testing import TestCase
from flask_sqlalchemy import SQLAlchemy

from chat.models.habit import Habit
from chat.models.success_log import SuccessLog

import tests.factories as factories

class TestViews(TestCase):
    def setUp(self):
        self.db.create_all()
        self.db.session.commit()

    def tearDown(self):
        self.db.drop_all()
        self.db.session.commit()

    def create_app(self):
        app = server.app
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
        self.db = SQLAlchemy(app)
        return app

    # def test_get(self):
    #     response = self.client.get("/")
    #     self.assertEqual(response.data, b'Not much to see here')
    #
    # @mock.patch('telegram.Bot')
    # def test_empty_post(self, mock):
    #     _str_request = '{"message": {"message_id": 12, "text": "aj", "from": {"last_name": "Krivich", "username": "Kiote", "id": 124557099, "first_name": "Ekaterina"}, "chat": {"last_name": "Krivich", "username": "Kiote", "id": 124557099, "type": "private", "first_name": "Ekaterina"}, "date": 1462140570}, "update_id": 627598290}'
    #     response = self.client.post("/", data=_str_request, content_type='application/json')
    #
    #     self.assertTrue("Kiote" in response.data.decode('utf-8'))
    #
    # @mock.patch('telegram.Bot')
    # def test_new_type(self, mock):
    #     self.db.session.query(Habit).delete()
    #     self.db.session.commit()
    #     _str_request = '{"message": {"message_id": 12, "text": "добавить new type", "from": {"last_name": "Krivich", "username": "Kiote", "id": 124557099, "first_name": "Ekaterina"}, "chat": {"last_name": "Krivich", "username": "Kiote", "id": 124557099, "type": "private", "first_name": "Ekaterina"}, "date": 1462140570}, "update_id": 627598290}'
    #
    #     response = self.client.post("/", data=_str_request, content_type='application/json')
    #     self.assertTrue("Поздравляю" in response.data.decode('utf-8'))
    #
    # @mock.patch('telegram.Bot')
    # def test_log_event(self, mock):
    #     self.db.session.query(SuccessLog).delete()
    #     self.db.session.commit()
    #     _str_request = '{"message": {"message_id": 12, "text": "успех", "from": {"last_name": "Krivich", "username": "Kiote", "id": 124557099, "first_name": "Ekaterina"}, "chat": {"last_name": "Krivich", "username": "Kiote", "id": 124557099, "type": "private", "first_name": "Ekaterina"}, "date": 1462140570}, "update_id": 627598290}'
    #     response = self.client.post("/", data=_str_request, content_type='application/json')
    #
    #     self.assertTrue("Отлично" in response.data.decode('utf-8'))

    @mock.patch('telegram.Bot')
    def test_succeed_today(self, mock):
        # create one success
        success = factories.SuccessLogFactory()

        ## TODO: make this one connected to just created success
        _str_request = '{"message": {"message_id": 12, "text": "успех", "from": {"last_name": "Krivich", "username": "Kiote", "id": 124557099, "first_name": "Ekaterina"}, "chat": {"last_name": "Krivich", "username": "Kiote", "id": 124557099, "type": "private", "first_name": "Ekaterina"}, "date": 1462140570}, "update_id": 627598290}'
        response = self.client.post("/", data=_str_request, content_type='application/json')

        print('*'*8)
        print(response.data.decode('utf-8'))
        print('*'*8)
        self.assertTrue("Сегодня" in response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
