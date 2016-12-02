from flask import Blueprint, render_template, redirect, url_for, request
from app import db
from models import User


routes = Blueprint('routes', __name__,
                   template_folder='templates')


@routes.route('/')
def hello():
    return render_template('index.html')


@routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(request.form['username'], request.form['password'])
        if user.is_valid():
            db.session.add(user)
            db.session.commit()
            flash('you are now registered', 'success')
            return redirect(url_for('login'))
        else:
            return render_template('register.html')
    else:
        return render_template('register.html')


@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            if 'username' not in request.form or 'password' not in request.form:
                return render_template('login.html', message={'error': "Username and password are required"})
            user = User.query.filter_by(username=request.form['username']).first()
            if user is None:
                return render_template('login.html', message={'error' : "Error"})
            if user.check_password(request.form['password']):
                flash('you are now signed in', 'success')
                return redirect(url_for('index'))
            else:
                return render_template('login.html', message={'error' : "Error"})
        except Exception as e:
            print(e)
            return render_template('login.html', message={'error' : "Error"})
    else:
        return render_template('login.html')