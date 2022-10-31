
from flask_wtf import FlaskForm
from datetime import datetime, date
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField,DateField,TimeField,SelectField

from wtforms.validators import InputRequired, Length, Email, EqualTo,DataRequired,ValidationError


#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")

#this is for register form
class EventForm(FlaskForm):
    event_name = StringField("Event Name", validators=[InputRequired('Enter event name')])
    event_start_date = DateField(label='startdate',format="%Y-%m-%d",validators = [DataRequired('please select event startdate')])
    event_end_date = DateField(label='enddate',format="%Y-%m-%d",validators = [DataRequired('please select event enddate')])
    event_start_time = TimeField(label='starttime')
    event_end_time = TimeField(label='endtime')
    event_type = SelectField(label='type')
    event_state = SelectField(label='states')





    