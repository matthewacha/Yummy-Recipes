from werkzeug.security import generate_password_hash, check_password_hash


class User(object):
    def __init__(self, first_name, last_name, email, password, category_name,category_description,
                 recipe_name, recipe_description, users=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.users = users
        self.category_name = category_name
        self.category_description = category_description
        self.recipe_name = recipe_name
        self.recipe_description = recipe_description
   
    def password_hsh(self, password):
       #generate password_hash
        self.password_hash = generate_password_hash(self.password)
		
    def verify_password(self, password):
        #check password with password_hash
        return check_password_hash(self.password_hash, password)
    
    def add_user(self):
        #creates a new user
        self.users.append(
            {
                'first_name':self.first_name,
                'last_name':self.last_name,
                'email':self.email,
                'password':self.password_hsh(self.password),
                'categories':{},
                'recipes':[]
            }
        )
        return self.users
    
    def find_user(self,email):
        #gets a user from the database
        for user in self.users:
            for key in user.keys():
                if user['email'] == self.email:
                    return user
                else:
                    return 'user doesnt exist'

    def list_user(self):
        for user in self.users:
            return user

    def add_category(self):
        #add category
        for user in self.users:
            for key in user.keys():
                if key == 'categories':
                    user['categories'] = {self.category_name:self.category_description}
                    return user['categories']

    def find_category(self, category_name):
        for user in self.users():
            if key == 'categories':
                for key in user['categories'].keys():
                    if key == self.category_name:
                        return key
                    
    def find_category_description(self,category_name):
        for user in self.users:
            for key in user.keys():
                if key == 'categories':
                    for key in user['categories'].keys():
                        if key == self.category_name:
                            return user['categories'][key]
                        return 'Category does not exist'

    def delete_category(self, category_name):
        for user in self.users:
            for key in user.keys():
                if key == 'categories':
                    for key in user['categories'].keys():
                        if key == self.category_name:
                            user['categories'].pop(self.category_name,None)
                            return user['categories']

    def add_recipe(self, recipe_name, recipe_description, category_name):
        for user in self.users:
            for key in user.keys():
                if key == 'recipes':
                    user['recipes'].append([{self.recipe_name:self.recipe_description},self.category_name])
                    return user['recipes']
                
    def view_recipe(self, recipe_name):
        for user in self.users:
            for key in user.keys():
                if key == 'recipes':
                    for item in user['recipes']:
                        for key in item[0].keys():
                            return item

    def delete_recipe(self, recipe_name):
        for user in self.users:
            for key in user.keys():
                if key == 'recipes':
                    for item in user['recipes']:
                        for key in item[0].keys():
                            if key == self.recipe_name:
                                user['recipes'].remove(item)
                                return user['recipes']
                                
