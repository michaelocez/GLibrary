from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Length, email


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), email(), Length(max=256)], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired(), Length(max=36)], render_kw={"placeholder": "Password"})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), email(), Length(max=256)], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired(), Length(max=36)], render_kw={"placeholder": "Password"})
    # makes sure 2nd password is same as 1st password
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password'), Length(max=36)], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Register')
