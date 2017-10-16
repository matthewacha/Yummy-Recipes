import unittest
from app import app


class TestsUsers(unittest.TestCase):
    #check tests work
    def test_registerpage(self):
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    #ensure user can signup
    def test_valid_register(self):
        tester = app.test_client(self)
        response = tester.post('/signup', data = dict(first_name='James',
                                                    last_name='King',
                                                    email= 'jk@gmail.com',
                                                    password='amazon'),
                               follow_redirects=True)
        self.assertIn(u'Congratulations, login to confirm your account',response.data)

    #ensure login works
    def test_loginpage(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertIn(u'Login',response.data)


    #ensure valid credentials login
    def test_valid_login(self):
        tester = app.test_client(self)
        tester.post('/signup', data = dict(first_name='James',
                                           last_name='King',
                                           email= 'jk@gmail.com',
                                           password='amazon'),
                    follow_redirects=True)
        response = tester.post('/login', data = dict(email='jk@gmail.com',password='amazon'),
                              follow_redirects=True)
        self.assertIn(u'Welcome',response.data)

    #ensure multiple users can login
    def test_multiple_login(self):
        tester = app.test_client(self)
        tester.post('/signup', data = dict(first_name='James',
                                           last_name='King',
                                           email= 'jk@gmail.com',
                                           password='amazon'),
                    follow_redirects=True)
        tester.post('/signup', data = dict(first_name='Andrew',
                                           last_name='Kyle',
                                           email= 'ak@gmail.com',
                                           password='amazon'),
                    follow_redirects=True)
        response = tester.post('/login', data = dict(email='ak@gmail.com',password='amazon'),
                              follow_redirects=True)
        self.assertIn(u'Welcome',response.data)

    #ensure multiple users login and logout
    def test_multiple_login(self):
        tester = app.test_client(self)
        tester.post('/signup', data = dict(first_name='James',
                                           last_name='King',
                                           email= 'jk@gmail.com',
                                           password='amazon'),
                    follow_redirects=True)
        tester.post('/signup', data = dict(first_name='Andrew',
                                           last_name='Kyle',
                                           email= 'ak@gmail.com',
                                           password='amazon'),
                    follow_redirects=True)
        tester.post('/login', data = dict(email='ak@gmail.com',password='amazon'),
                              follow_redirects=True)
        tester.post('/logout',follow_redirects=True)
        response = tester.post('/login', data = dict(email='jk@gmail.com',password='amazon'),
                              follow_redirects=True)
        self.assertIn(u'Welcome',response.data)
    

    #ensure wrong password does not login in
    def  test_invalid_login(self):
        tester = app.test_client(self)
        tester.post('/signup', data = dict(first_name='James',
                                           last_name='King',
                                           email= 'jk@gmail.com',
                                           password='amazon'),
                    follow_redirects=True)
        response = tester.post('/login', data = dict(email='jk@gmail.com',password='amazonia'),
                              follow_redirects=True)
        self.assertIn(u'Wrong password',response.data)

    #ensure wrong email does not login in
    def  test_invalid_login(self):
        tester = app.test_client(self)
        tester.post('/signup', data = dict(first_name='James',
                                           last_name='King',
                                           email= 'jk@gmail.com',
                                           password='amazon'),
                    follow_redirects=True)
        response = tester.post('/login', data = dict(email='jkm@gmail.com',password='amazon'),
                              follow_redirects=True)
        self.assertIn(u'Wrong email',response.data)

    #ensure logout works
    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/signup', data = dict(first_name='James',
                                           last_name='King',
                                           email= 'jk@gmail.com',
                                           password='amazon'),
                    follow_redirects=True)
        tester.post('/login', data = dict(email='jk@gmail.com',password='amazon'),
                    follow_redirects=True)
        response = tester.post('/logout',follow_redirects=True)
        self.assertIn(u'You must login again',response.data)

    #ensure logout only possible when logged in
    def test_invalid_logout(self):
        tester = app.test_client(self)
        response = tester.post('/logout',follow_redirects=True)
        self.assertIn(u'You need to be logged in',response.data)

class TestsRecipes(unittest.TestCase):
    #ensure tests work
    def test_recipepage(self):
        tester = app.test_client(self)
        response = tester.get('/recipe', content_type ='html/text',follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    #ensure access only to logged in user    
    def test_invalid_recipe_access(self):
        tester = app.test_client(self)
        response = tester.get('/recipe', content_type ='html/text',follow_redirects=True)
        self.assertIn(u'You need to be logged in', response.data)

    #ensure logged in user can add recipe
    def test_valid_add_recipepage(self):
        tester = app.test_client(self)
        tester.post('/signup', data = dict(first_name='James',
                                           last_name='King',
                                           email= 'jk@gmail.com',
                                           password='amazon'),
                    follow_redirects=True)
        tester.post('/login', data = dict(email='jk@gmail.com',password='amazon'),
                              follow_redirects=True)
        response = tester.get('/recipe/add')
        self.assertEqual(response.status_code, 200)
        
    #ensure non-logged in user cant add recipe
    def test_invalid_add_recipe(self):
        tester = app.test_client(self)
        response = tester.get('/recipe/add', follow_redirects=True)
        self.assertIn(u'You need to be logged in', response.data)
        

    #ensure user can add recipe
    def test_valid_add_recipe(self):
        tester = app.test_client(self)
        tester.post('/signup', data = dict(first_name='James',
                                           last_name='King',
                                           email= 'jk@gmail.com',
                                           password='amazon'),
                    follow_redirects=True)
        tester.post('/login', data = dict(email='jk@gmail.com',password='amazon'),
                              follow_redirects=True)
        tester.post('/recipe/add', data = dict(recipe_name='Beans and peas',
                                                          recipe_description='add salt'),
                               follow_redirects=True)
        response = tester.post('/recipe/add', data = dict(recipe_name='Sea Food',
                                                          recipe_description='add oil and simmer'),
                               follow_redirects=True)
        self.assertIn(u'Sea Food', response.data)
        self.assertIn(u'Beans and peas', response.data)
        self.assertIn(u'2', response.data)


    #ensure non-logged in user cant edit recipe
    def test_unauthoriesd_edit(self):
        tester = app.test_client(self)
        response = tester.get('/recipe/edit/<recipe_name>', follow_redirects=True)
        self.assertIn(u'You need to be logged in', response.data)

    #ensure user can edit recipe
    def test_edit_recipe(self):
        tester = app.test_client(self)
        tester.post('/signup', data = dict(first_name='James',
                                           last_name='King',
                                           email= 'ak@gmail.com',
                                           password='amazon'),
                    follow_redirects=True)
        tester.post('/login', data = dict(email='ak@gmail.com',password='amazon'),
                              follow_redirects=True)
        tester.post('/recipe/add', data = dict(recipe_name='Beans and peas',
                                                          recipe_description='add salt'),
                               follow_redirects=True)
        tester.post('/recipe/add', data = dict(recipe_name='Sea Food',
                                               recipe_description='add oil and simmer'),
                    follow_redirects=True)
        response = tester.post('recipe/edit/Sea Food', data=dict(recipe_name='Sea and lake Foods',
                                                                 recipe_description='simmer for two minutes'),
                               follow_redirects=True)
        self.assertIn(u'Sea and lake Foods', response.data)
        self.assertIn(u'Sea Food', response.data)

    #ensure non-logged in user cant delete recipe
    def test_unauthorised_delete_recipe(self):
        tester = app.test_client(self)
        response = tester.post('/recipe/delete/<recipe_name>',follow_redirects=True)
        self.assertIn(u'You need to be logged in', response.data)

    #ensure logged in user can delete recipe
    def test_authorised_delete_recipe(self):
        tester = app.test_client(self)
        tester.post('/signup', data = dict(first_name='James',
                                           last_name='King',
                                           email= 'jk@gmail.com',
                                           password='amazon'),
                    follow_redirects=True)
        tester.post('/login', data = dict(email='jk@gmail.com',password='amazon'),
                              follow_redirects=True)
        tester.post('/recipe/add', data = dict(recipe_name='Beans and peas',
                                                          recipe_description='add salt'),
                               follow_redirects=True)
        tester.post('/recipe/add', data = dict(recipe_name='Sea Food',
                                               recipe_description='add oil and simmer'),
                    follow_redirects=True)
        response = tester.post('recipe/delete/Sea Food',
                               follow_redirects=True)
        self.assertIn(u'Successfully deleted', response.data)
        
if __name__=='__main__':
    unittest.main()
