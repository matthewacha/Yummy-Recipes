import unittest
import models
from models import User
class ModelsTest(unittest.TestCase):
    def setUp(self):
        self.first_name = 'James'
        self.last_name = 'Clark'
        self.email = 'jc@gmail.com'
        self.password = 'amazon'
        self.category_name = 'cakes and pasteries'
        self.category_description = 'these are awesome cakes for all'
        self.recipe_name = 'chicken soup'
        self.recipe_description = 'chicken breast, garlic'
        self.user = User(self.first_name, self.last_name,
                         self.email, self.password, self.category_name,
                         self.category_description,self.recipe_name,self.recipe_description, users=[])
                              
    ##Test cases
    def test_add_user(self):
        self.assertEqual(self.user.add_user('James', 'Clark', 'js@gmail.com', 'amazon'), [{'first_name':self.first_name, 'last_name':self.last_name,
                                                 'email':self.email,
                                                 'password':self.user.password_hsh(self.password),
                                                 'categories':{},
                                                 'recipes':[]}])
    def test_find_user(self):
        self.user.add_user('James', 'Clark', 'js@gmail.com', 'amazon')
        self.assertEqual(self.user.find_user('jc@gmail.com'),{'first_name':self.first_name, 'last_name':self.last_name,\
                              'email':self.email,'password':self.user.password_hsh(self.password),\
                              'categories':{},'recipes':[]})
    def test_add_category(self):
        self.user.add_user('James', 'Clark', 'js@gmail.com', 'amazon')
        self.assertEqual(self.user.add_category('cakes and pasteries', 'these are awesome cakes for all'),True)

    def test_list_categories(self):
        self.user.add_user('James', 'Clark', 'js@gmail.com', 'amazon')
        self.user.add_category('cakes and pasteries', 'these are awesome cakes for all')
        self.assertEqual(self.user.list_categories(),{'cakes and pasteries': 'these are awesome cakes for all'})

    def test_find_category_description(self):
        self.user.add_user('James', 'Clark', 'js@gmail.com', 'amazon')
        self.user.add_category('cakes and pasteries', 'these are awesome cakes for all')
        self.assertEqual(self.user.find_category_description('cakes and pasteries'),'these are awesome cakes for all')

    def test_delete_category(self):
        self.user.add_user('James', 'Clark', 'js@gmail.com', 'amazon')
        self.user.add_category('cakes and pasteries', 'these are awesome cakes for all')
        self.assertEqual(self.user.delete_category('cakes and pasteries'),{})

    def test_add_recipe(self):
        self.user.add_user('James', 'Clark', 'js@gmail.com', 'amazon')
        self.user.add_category('cakes and pasteries', 'these are awesome cakes for all')
        self.recipe_name = 'chicken soup'
        self.recipe_description = 'chicken breast, garlic'
        self.assertEqual(self.user.add_recipe('chicken soup', 'chicken breast, garlic', 'chickens and ducks'),
                         [[{'chicken soup':'chicken breast, garlic'},'cakes and pasteries']] )

    def test_view_recipe(self):
        self.user.add_user('James', 'Clark', 'js@gmail.com', 'amazon')
        self.user.add_category('cakes and pasteries', 'these are awesome cakes for all')
        self.user.add_recipe('chicken soup', 'chicken breast, garlic', 'chickens and ducks')
        self.assertEqual(self.user.view_recipe('chicken soup'),[{'chicken soup':'chicken breast, garlic'},'cakes and pasteries'] )

    def test_delete_recipe(self):
        self.user.add_user('James', 'Clark', 'js@gmail.com', 'amazon')
        self.user.add_category('cakes and pasteries', 'these are awesome cakes for all')
        self.user.add_recipe('chicken soup', 'chicken breast, garlic', 'chickens and ducks')
        self.assertEqual(self.user.delete_recipe('chicken soup'), [])

if __name__ == '__main__':
    unittest.main()
