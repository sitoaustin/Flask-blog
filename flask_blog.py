from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ee6927c7fc78a6e79ac0d3fd1d4054f9'

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
