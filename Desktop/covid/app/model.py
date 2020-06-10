from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class Country:
    '''
    Source class to define Source Objects
    '''
    def __init__(self,country,cases,todayCases,deaths,todayDeaths,recovered,active,critical):
        self.country =country
        self.cases=cases
        self.todayCases=todayCases
        self.deaths=deaths
        self.todayDeaths=todayDeaths
        self.recovered=recovered
        self.active=active
        self.critical=critical

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    def __repr__(self):
        return f'User {self.username}' 
        
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)   
class Coronavirus():
    def __init__(self):
        self.driver = webdriver.Chrome()                    