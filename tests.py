"""test user blueprint"""
import os
import unittest
from flask import url_for
from app import app, yummy


TEST_DB = 'test_db'
BASEDIR = os.path.abspath(os.path.dirname(__file__))

class BasicTest(unittest.TestCase):
    def setUp(self):
        """setup executed at start of each testcase"""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLE'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+\
        os.path.join(BASEDIR, 'TEST_DB')
        app.config['SERVER_NAME'] = 'localhost:5000'
        self.app = app.test_client()
        yummy.drop_all()
        yummy.create_all()
     
    def tearDown(self):
        """executed after each test"""
        pass 
		
    ##helper methods##
    def register(self,first_name, last_name, email, password):
	    return self.app.post('/signup', data=dict(first_name = first_name,\
		                      last_name = last_name, email = email, password = password)\
							  ,follow_redirects = True)
	
    def login(self, email, password):
        return self.app.post('/login', data = dict(email = email, password = password)\
		                      ,follow_redirects = True)
    ##tests##
    def test_signup_page(self):
        response = self.app.get('/signup')
        self.assertEqual(response.status_code, 200)
    def test_signup_form_displays(self):
        response = self.app.get('/signup')
        self.assertIn(b'Last name:', response.data)	
    def test_valid_signup(self):
        self.app.get('/signup')
        response = self.register('James', 'King', 'kj@gmail.com', 'marsRocks')
        self.assertIn(b'Congratulations,login to confirm your account', response.data)		
		
    def test_login_page(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code,200)
    def test_valid_login(self):
        self.register('James', 'King', 'kj@gmail.com', 'marsRocks')    
        response = self.login('kj@gmail.com', 'marsRocks')
        self.assertIn(b'Welcome', response.data)
    
		
if __name__ == '__main__':
    unittest.main()
