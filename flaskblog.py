from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5835fd78b0a7bf27926bc3f7b0d0927d'

posts = [
    {
        'author': 'Sri Iyer',
        'title': 'First blog post',
        'content': 'First blog content',
        'date_posted': '12, September 2019'
    },
    {
        'author': 'Ram Kumar',
        'title': 'Second blog post',
        'content': 'Second blog content',
        'date_posted': '10, July 2019'
    },
    {
        'author': 'Rob Weiner',
        'title': 'Third blog post',
        'content': 'Third blog content',
        'date_posted': '7, February 2019'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
