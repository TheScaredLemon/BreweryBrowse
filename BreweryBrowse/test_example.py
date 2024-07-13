import unittest
from app import app, db
from models import ExampleModel

class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_examples(self):
        response = self.app.get('/example')
        self.assertEqual(response.status_code, 200)

    def test_create_example(self):
        response = self.app.post('/example', json={'name': 'Test', 'value': '123'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test', response.get_json()['name'])

if __name__ == '__main__':
    unittest.main()
