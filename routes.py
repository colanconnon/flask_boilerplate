from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from models import User
from forms import RegistrationForm, LoginForm

routes = Blueprint('routes', __name__,
                   template_folder='templates')


@routes.route('/')
def index():
    return render_template('index.html')


@routes.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(request.form['username'], request.form['password'])
        if user.is_valid():
            db.session.add(user)
            db.session.commit()
            flash('you are now registered', 'success')
            return redirect(url_for('login'))
    return render_template('register.html', form=form)


@routes.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        print(request.form['email'])
        user = User.query.filter_by(
            username=request.form['email']).first()
        if user is None:
            return render_template('login.html', form=form,
                                   message={'error': "Username and password are incorrect"})
        if user.check_password(request.form['password']):
            flash('you are now signed in', 'success')
            return redirect(url_for('index'))
        else:
            return render_template('login.html', form=form,
                                   message={'error': "Username and password are incorrect"})
    else:
        return render_template('login.html', form=form)
