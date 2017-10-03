from werkzeug.security import generate_password_hash, check_password_hash


class User(object):
    def __init__(self, first_name, last_name, email, password, category_name,category_description,
                 users=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.users = users
        self.category_name = category_name
        self.category_description = category_description
   
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
                'recipes':{}
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
    def find_category(self):
        for user in self.users:
            for key in user.keys():
                if key == 'categories':
                    return user['categories'][self.category_name]
                
class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def add_category(self):
        for user in user_db:
            return user
            for key in user.keys():
                if user['categories']:
                    user['categories'] = {self.name:self.description}
                    return user['categories']
                    
    def find_category(self, name):
        for user in users:
            for key in user.iterKeys():
                if key == 'categories':
                    for key in user['categories'].iterKeys():
                        if key == self.name:
                            return key
                        
    def delete_category(self, name):
        user.pop(User.find_category(self.name))
         
    def show_categories(self):
        for user in users:
            for key in user.iterKeys():
                if key == 'categories':
                    return key
		
class Recipe(User):
    def __init__(self, name, description, category_name):
        self.name = name 
        self.description = description

        def add_recipe(self, name, description):
            for user in users:
                for key in user.iterKey:
                    if key == 'recipes':
                        user['recipes'] = {[self.name, self.description]:self.category_name}

        def find_recipe(self, name):
            for user in users:
                for key in user.iterKeys():
                    if key == 'recipes':
                        recipe_info = user['recipes']
                        for k in recipe_info.iterKeys(): 
                            if  k[0] == self.name:
                                return k
        def delete_recipe(self, name):
            for user in users:
                for key in user.iterKeys():
                    if key == 'recipes':
                        recipe_info = user['recipes']
                        for k in recipe_info.iterKeys(): 
                            if  k[0] == self.name:
                                del recipe_info[k[0]]
