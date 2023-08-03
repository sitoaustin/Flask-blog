from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)

app.config['SECRET_KEY'] = 'ee6927c7fc78a6e79ac0d3fd1d4054f9'
# To SET our data base location (sqlite:/// - path where we want out database to be)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
# to create a database instance
db = SQLAlchemy(app)
bcrypt = Bcrypt()

# Initializing our login Manager
# it handles all the session in the background for us
login_manager = LoginManager(app)
# Login manager to set our login route and the 'login' is our login route function
login_manager.login_view = 'login'
# the info I think is bootstrap info class in our login alert
login_manager.login_message_category = 'info'

from flask_blog import routes