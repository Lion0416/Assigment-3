
from re import M
from flask_wtf import FlaskForm
from datetime import datetime, date
from traitlets import default
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, DateField, TimeField, EmailField, SelectField, IntegerField
from flask_wtf.file import FileRequired, FileField, FileAllowed
from wtforms.validators import InputRequired, Length, Email, EqualTo,DataRequired


#creates the login information
class LoginForm(FlaskForm):
    emailid=StringField("Email Address", validators=[InputRequired('Enter your Email Address')])
    password=PasswordField("Password", validators=[InputRequired('Enter your Password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    userName=StringField("User Name", validators=[InputRequired()])
    emailid = EmailField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired()])
    confirm=PasswordField("Confirm Password", validators=[InputRequired()])
    contactNumber = StringField("Contact Number", validators=[InputRequired()])
    address =StringField("Address of Residence", validators=[InputRequired()])
    #submit button
    submit = SubmitField("Register")


#this is for register form
ALLOWED_FILE = {'PNG','JPG','png','jpg'}

class EventForm(FlaskForm):
    event_name = StringField("Event Name", validators=[InputRequired('Enter event name')])
    event_start_date = DateField(label='Event Starting Date',validators = [DataRequired('please select event startdate')])
    event_end_date = DateField(label='Event Ending Date',validators = [DataRequired('please select event enddate')])
    event_start_time = TimeField(label='Event Starting Time')
    event_end_time = TimeField(label='Event Ending Time')
    event_type = SelectField(label='type',choices=[])
    event_state = SelectField(label='states', choices=[])
    eventimage = FileField('Upload an Event Image')
    #eventimage = FileField('Upload an Event Image', validators=[FileRequired(message='An Image Must Be Selected to Create an Event'), FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
    #eventimage = FileField('Event Image', validators=[
    #FileRequired(message='Image cannot be empty'),
    #FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
    event_location = StringField("Event Location", validators=[InputRequired('Enter event location')])
    description = TextAreaField('Description', validators=[InputRequired()])
    ticketPrice = StringField('Ticket Price', validators=[InputRequired()])
    ticketQuantity = StringField('Ticket Quantity', validators=[InputRequired()])
    submit = SubmitField('Publish Event')



#User comment
class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()])
  submit = SubmitField('Create')



class TicketPurchaseForm(FlaskForm):
    ticketQuantity = IntegerField('Ticket Quantity', [InputRequired()])
    submit = SubmitField('Purchase')

    