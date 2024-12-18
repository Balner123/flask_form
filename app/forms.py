# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Regexp

class UserForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message='Username is required.'),
        Regexp(r'^[\w]+$', message='Username must contain only letters, numbers, and underscores.')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required.'),
        Regexp(r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$', message='Password must contain at least one uppercase letter, one number, and one special character.')
    ])
    submit = SubmitField('Add User')