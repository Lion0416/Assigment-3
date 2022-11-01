from asyncio import events
from tkinter import EventType
from datetime import datetime, date
from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from .models import Event,Comment
from .forms import EventForm,CommentForm
from . import db
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
import os

bp = Blueprint('event', __name__, url_prefix='/event')

@bp.route('/<eventid>')
def show(id):

    return render_template('destinations/show.html')


@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
  print('Method type: ', request.method)
  form = EventForm()
  
  if form.validate_on_submit():
    #call the function that checks and returns image
    db_file_path=check_upload_file(form)
    print(form.event_start_time)
    
    #event_start_time=datetime.strptime(str(form.event_start_time.data), '%H:%M')
    #event_end_time=datetime.strptime(str(form.event_end_time.data), '%H:%M')
    event=Event(eventName=form.event_name.data,description=form.description.data,
    eventstartDate=form.event_start_date,eventendDate=form.event_end_date,
    eventstartTime=form.event_start_time.data,eventendTime=form.event_end_time.data,
    eventType=form.event_type,eventStates=form.event_state,
    eventImage=db_file_path,ticketPrice=form.ticketPrice.data,ticketQuantity=form.ticketQuantity.data)
    # add the object to the db session
    db.session.add(event)
    # commit to the database
    db.session.commit()
    print('Successfully created new event', 'success')
    #Always end with redirect when form is valid
    return redirect(url_for('event.create'))
  return render_template('event/create.html', form=form)


def check_upload_file(form):
  #get file data from form  
  fp=form.eventimage.data
  filename=fp.filename
  #get the current path of the module file… store image file relative to this path  
  BASE_PATH=os.path.dirname(__file__)
  #upload file location – directory of this file/static/image
  upload_path=os.path.join(BASE_PATH,'static/image',secure_filename(filename))
  #store relative path in DB as image location in HTML is relative
  db_upload_path='/static/image/' + secure_filename(filename)
  #save the file and return the db upload path  
  fp.save(upload_path)
  return db_upload_path



@bp.route('/<destination>/comment', methods = ['GET', 'POST'])  
@login_required
def comment(event):  
    form = CommentForm()  
    #get the destination object associated to the page and the comment
    event_obj = Event.query.filter_by(id=event).first()  
    if form.validate_on_submit():  
      #read the comment from the form
      comment = Comment(text=form.text.data,  
                        event=event_obj,
                        user=current_user) 
      #here the back-referencing works - comment.destination is set
      # and the link is created
      db.session.add(comment) 
      db.session.commit() 

      #flashing a message which needs to be handled by the html
      #flash('Your comment has been added', 'success')  
      print('Your comment has been added', 'success') 
    # using redirect sends a GET request to destination.show
    return redirect(url_for('destination.show', id=event))