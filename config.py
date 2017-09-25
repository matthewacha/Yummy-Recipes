import os
#define directory for application
BASEDIR= os.path.abspath(os.path.dirname(__file__))

class configBase():
    DEBUGING = True
    SQLALCHEMY_DATABASE_URI='postgresql///'\
    +os.path.join(BASEDIR,'yummy_db')
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'Xmas1945Mars'

 
class Developer(configBase): 
    #for development purposes
    SQLALCHEMY_DATABASE_URI='sqlite///'\
    +os.path.join(BASEDIR,'yummy_db')
    WTF_CSRF_ENABLED = True
	
	