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
    
    ##tests##
    def test_signup_page(self):
        response = self.app.get('/signup')
        self.assertEqual(response.status_code, 200)
		
    def test_login_oage(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code,200)
        
    
		
if __name__ == '__main__':
    unittest.main()
