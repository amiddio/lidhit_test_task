import os

from django.test import TestCase, override_settings
from django.conf import settings
from tinydb import TinyDB


@override_settings(DB_NAME=settings.TEST_DB_NAME)
class FormCheckerViewTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        with TinyDB(settings.DB_NAME) as db:
            forms = [
                {
                    'name': 'Auth Form',
                    'customer_email': 'email', 'password': 'text'
                }
            ]
            for item in forms:
                db.insert(item)

    def test_request_get_form(self):
        res = self.client.post(
            '/get_form',
            data={'customer_email': 'j.dow@home.local', 'password': '12345'}
        )
        self.assertEqual(200, res.status_code)

    def test_request_get_form_negative(self):
        res = self.client.get('/get_form?fname=val1&lname=val2')
        self.assertNotEqual(200, res.status_code)

    @classmethod
    def tearDownClass(cls):
        try:
            open(settings.TEST_DB_NAME, 'w').close()
            os.remove(settings.TEST_DB_NAME)
        except Exception as e:
            print(e)
