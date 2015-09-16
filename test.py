__author__ = 'hanyuen'

from app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_login_page_load(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue("Train Booking need login" in response.data)

    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(user="admin", password="pass111word"), follow_redirects=True )
        self.assertTrue("logout" in response.data)

    def test_trains_showup(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(user="admin", password="pass111word"), follow_redirects=True )
        self.assertIn("ottawa" in response.data)


if __name__ == '__main__':
    unittest.main()


#Run test in shell command
# python test.py -v