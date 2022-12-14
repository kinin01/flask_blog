from distutils.log import debug
from email.policy import default
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']= '432da3bc4dacd1ccf6b8797cc03c4821'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app) 
login_manager= LoginManager(app)
login_manager. Login_view = 'login'
login_manager. login_message_category = 'info'


from flaskblog import routes