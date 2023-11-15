import os

from django.conf import settings
from django.test import TestCase, override_settings
from tinydb import TinyDB

from .. services.form_checker_service import FormCheckerService
from .. services.tinydb_data_source import TinydbDataSource


@override_settings(DB_NAME=settings.TEST_DB_NAME)
class FormCheckerServiceTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        with TinyDB(settings.DB_NAME) as db:
            forms = [
                {
                    'name': 'Customer Form',
                    'f_name': 'text', 'l_name': 'text', 'email': 'email', 'phone': 'phone', 'dob': 'date',
                },
                {
                    'name': 'Callme Form',
                    'full_name': 'text', 'phone': 'phone', 'date': 'date',
                },
                {
                    'name': 'Order Form',
                    'full_name': 'text', 'phone': 'phone', 'email': 'email', 'price': 'text'
                },
                {
                    'name': 'Auth Form',
                    'customer_email': 'email', 'password': 'text'
                },
            ]
            for item in forms:
                db.insert(item)

    def test_request_data_success_1(self):
        data = {
            'customer_email': 'j.dow@home.local', 'password': '12345'
        }
        service = FormCheckerService(data_source=TinydbDataSource(data=data))
        res = service.search()
        self.assertEqual('Auth Form', res)

    def test_request_data_success_2(self):
        data = {
            'email': 'j.dow@home.local', 'full_name': 'john dow', 'phone': '+7 111 222 33 44', 'price': '15.45'
        }
        service = FormCheckerService(data_source=TinydbDataSource(data=data))
        res = service.search()
        self.assertEqual('Order Form', res)

    def test_request_data_success_3(self):
        data = {
            'full_name': 'john dow', 'phone': '+7 111 222 33 44', 'date': '01.05.2000'
        }
        service = FormCheckerService(data_source=TinydbDataSource(data=data))
        res = service.search()
        self.assertEqual('Callme Form', res)

    def test_request_data_success_4(self):
        data = {
            'full_name': 'john dow', 'phone': '+7 111 222 33 44', 'date': '2000-05-01'
        }
        service = FormCheckerService(data_source=TinydbDataSource(data=data))
        res = service.search()
        self.assertEqual('Callme Form', res)

    def test_request_data_negatives_1(self):
        data = {
            'full_name': 'john dow', 'phone': '+7 1110 222 33 44', 'date': '2000-05-01'
        }
        service = FormCheckerService(data_source=TinydbDataSource(data=data))
        res = service.search()
        self.assertEqual({'full_name': 'text', 'phone': 'text', 'date': 'date'}, res)

    def test_request_data_negatives_2(self):
        data = {
            'full_name': 'john dow', 'value_phone': '+7 111 222 33 44', 'value_date': '2000-05-01'
        }
        service = FormCheckerService(data_source=TinydbDataSource(data=data))
        res = service.search()
        self.assertEqual({'full_name': 'text', 'value_date': 'date', 'value_phone': 'phone'}, res)

    def test_request_data_negatives_3(self):
        data = {
            'f_name1': 'qwerty', 'f_name2': '+7 111 222 33 44', 'f_name3': 'myemail@home.local'
        }
        service = FormCheckerService(data_source=TinydbDataSource(data=data))
        res = service.search()
        self.assertEqual({'f_name1': 'text', 'f_name2': 'phone', 'f_name3': 'email'}, res)

    @classmethod
    def tearDownClass(cls):
        try:
            open(settings.TEST_DB_NAME, 'w').close()
            os.remove(settings.TEST_DB_NAME)
        except Exception as e:
            print(e)



