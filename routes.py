from flask import render_template, request, flash, redirect
from flask import Blueprint
from models import User, Url, db
from flask_login import login_user, logout_user, current_user
from bs4 import BeautifulSoup
import requests

routes = Blueprint('routes', __name__)

def load_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    return user

@routes.route('/', methods=['GET', 'POST'])
def home():
    short_url = None
    if request.method == 'POST':
        long_url = request.form['long_url']

        if long_url:
            url = Url.query.filter_by(long_url=long_url).first()

            if url:
                short_url = request.host_url + url.random_string
            else:
                new_url = Url(long_url=long_url,
                              user_id=current_user.id)
                db.session.add(new_url)
                db.session.commit()
                short_url = request.host_url + new_url.random_string
        else:
            flash('Please enter an URL to shorten', 'error')
            return redirect('/')

    return render_template('home.html', short_url=short_url)


@routes.route('/<string:random_string>')
def short_url(random_string):
    url = Url.query.filter_by(random_string=random_string).first_or_404()
    return redirect(url.long_url)

@routes.route('/<username>/shortened_urls')
def display_shortened_urls(username):
    if not current_user.is_authenticated:
        flash("You are not authorized to view this page. Please log in.", "error")
        return redirect('/login')
    
    user = load_user_by_username(username)
    urls = user.urls

    for url in urls:
        response = requests.get(url.long_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string
            url.title = title
            
    return render_template('shortened_urls.html', user=user, urls=urls)


@routes.route('/register', methods=['GET', 'POST'])
def register():
    if not current_user.is_authenticated:
        if request.method == 'POST':
            name = request.form['name']
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']

            check_username = User.query.filter_by(username=username).first()
            check_email = User.query.filter_by(email=email).first()

            if not all([name, username, email, password]):
                flash("Please fill out all fields", "error")
                return redirect('/register')

            elif check_username:
                flash("Username already exists", "error")
                return redirect('/register')

            elif check_email:
                flash("Email already exists", "error")
                return redirect('/register')

            elif len(password) < 8:
                flash("Password must be at least 8 characters", "error")
                return redirect('/register')

            else:
                new_user = User(name=name, username=username, email=email)
                new_user.set_password(password)
                db.session.add(new_user)
                db.session.commit()
                flash("User created successfully", "success")
                return redirect('/login')
        else:
            return render_template('auth/register.html')
    else:
        flash("You are already logged in", "error")
        return redirect('/')


@routes.route('/login', methods=['GET', 'POST'])
def login():
    if not current_user.is_authenticated:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            check_user = User.query.filter_by(username=username).first()

            if not all([username, password]):
                flash("Please fill out all fields", "error")
                return redirect('/login')

            elif check_user and check_user.check_password(password):
                login_user(check_user)
                flash("Logged in successfully", "success")
                return redirect('/')

            else:
                flash("Username or password is incorrect", "error")
                return redirect('/login')
        else:
            return render_template('auth/login.html')
    else:
        flash("You are already logged in", "error")
        return redirect('/')


@routes.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash("Logged out successfully", "success")
        return redirect('/login')
    else:
        flash("You are not logged in", "error")
        return redirect('/login')
    
@routes.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
