from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SECRET_KEY'] = 'ee6927c7fc78a6e79ac0d3fd1d4054f9'
# To SET our data base location (sqlite:/// - path where we want out database to be)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
# to create a database instance
db = SQLAlchemy(app)

# To create our models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # db.relationship...
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # db.ForeignKey specifies that our user_Id has a relationship with our UserModel
    # our 'user.id' is lowercase because we are referencing the table and column name
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


posts =[
    {
        'author': 'Naka',
        "title": 'Blog Post 1',
        'content': 'First post content',
        'data_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        "title": 'Blog Post 2',
        'content': 'Second post content',
        'data_posted': 'April 21, 2018'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title='Home Page')

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', "success")
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
