from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo

class SignupForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired("You must have a username"), Length(4, 20, "Usernames must be between 4-20 characters long")])
    password = PasswordField("Password", validators=[InputRequired("You must have a password"), Length(10, message="Your password must be at least 10 characters long")])
    confirm_password = PasswordField("Confirm Password", validators=[EqualTo("password")])
    submit = SubmitField()

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
    submit = SubmitField()