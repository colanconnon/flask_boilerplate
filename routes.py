from flask import Blueprint, render_template, redirect, url_for, request, flash
from forms import RegistrationForm, LoginForm, TodoForm

app_routes = Blueprint('app_routes', __name__,
                   template_folder='templates')
from database import db
from models import User, Todo


@app_routes.route('/')
def index():
    return render_template('index.html')

@app_routes.route('/todo', methods=['GET'])
def todos():
    todos = Todo.query.all()
    return render_template('todos.html', todos=todos)

@app_routes.route('/todo/<id>', methods=['GET'])
def todo(id):
    todo = Todo.query.get(id)
    return render_template('todo.html', todo=todo)

@app_routes.route('/create-todo', methods=['GET', 'POST'])
def create_todo():
    form = TodoForm(request.form)
    if request.method == 'POST' and form.validate():
        todo = Todo(request.form['name'])
        db.session.add(todo)
        db.session.commit()
        flash(f'Created Todo with id {todo.id}', 'success')
        return redirect('/todo')
    return render_template('createtodo.html', form=form)

@app_routes.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(request.form['email'], request.form['password'])
        if user.is_valid():
            db.session.add(user)
            db.session.commit()
            flash('you are now registered', 'success')
            return redirect('/login')
        else:
            return render_template('register.html', form=form,
                                    message={'error': "Invalid input provided"})
    return render_template('register.html', form=form)


@app_routes.route('/login', methods=['GET', 'POST'])
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
