from flask import render_template
from application import app

@app.route('/')
@app.route('/home')
def home():
 return render_template('home.html', title='Home')

@app.route('/')
@app.route('/about')
def home():
 return render_template('about.html', title='About')

@app.route('/')
@app.route('/account')
def about():
 return render_template('about.html', title='About')

@app.route('/')
@app.route('/account')
def account():
 return render_template('account.html', title='Account')

@app.route('/')
@app.route('/collection')
def collection():
 return render_template('collection.html', title='Collection')

@app.route('/')
@app.route('/login')
def login():
 return render_template('login.html', title='Login')

@app.route('/')
@app.route('/register')
def register():
 return render_template('register.html', title='Register')