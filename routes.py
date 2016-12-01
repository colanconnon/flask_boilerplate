from flask import Blueprint, render_template, redirect, url_for
from models import User
from app import db


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
        user = User.filter_by(username=request.form['username']).first()
        if user.check_password(request.form['password']):
            flash('you are now signed in', 'success')
            return redirect(url_for('index'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')