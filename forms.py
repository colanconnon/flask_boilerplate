from wtforms import Form, BooleanField, StringField, PasswordField, validators


class RegistrationForm(Form):
    email = StringField('Email Address', [validators.DataRequired(
        message="You must provide an email")])
    password = PasswordField('New Password', [
        validators.Length(
            min=6, message="Password must be atleast 6 characters long"),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')


class LoginForm(Form):
    email = StringField(
        'Email Address', [validators.DataRequired(message="Email is required")])
    password = PasswordField('New Password',
                             [validators.DataRequired(message="Password is required")])
