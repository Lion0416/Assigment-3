from asyncio import events
from datetime import datetime, date
from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from .models import Event, Comment, Order
from .forms import EventForm, CommentForm, TicketPurchaseForm
from . import db
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
import os
from .models import Type,States

bp = Blueprint('event', __name__, url_prefix='/event')

@bp.route('/<id>', methods = ['GET', 'POST'])
def show(id):
  #event = db.session.query(Event, Type, States).select_from(Event).join(Type).join(States).filter(Event.eventid == id).first()
  event = Event.query.filter(Event.eventid == id).first()

  bform = TicketPurchaseForm()
  cform = CommentForm()

  if bform.validate_on_submit():

    event = Event.query.filter(Event.eventid == id).first()
    event.ticketsAvailable = int(event.ticketsAvailable) - bform.ticketQuantity.data
    db.session.commit()

    order=Order(
      ticketQuantity=bform.ticketQuantity.data,
      totalCost=int(bform.ticketQuantity.data) * event.ticketPrice,
      orderDate=date.today(),
      userid=current_user.id,
      eventid=event.eventid
    )

    db.session.add(order)
    db.session.commit()
  return render_template('events/show.html', event = event, form = cform, form2 = bform)

@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
  form = EventForm()
  form.event_type.choices = [(type.typeid,type.type) for type in Type.query.all()]
  form.event_state.choices = [(states.statesid,states.states) for states in States.query.all()]
  
  if form.validate_on_submit():
    #call the function that checks and returns image
    db_file_path=check_upload_file(form)
    event=Event(
      userid = current_user.id,
      eventName=form.event_name.data,
      eventLocation=form.event_location.data,
      description=form.description.data,
      eventstartDate=form.event_start_date.data,
      eventendDate=form.event_end_date.data,
      eventstartTime=form.event_start_time.data,
      eventendTime=form.event_end_time.data,
      eventType=form.event_type.data,
      eventStates=form.event_state.data,
      eventImage=db_file_path,
      ticketPrice=form.ticketPrice.data,
      ticketQuantity=form.ticketQuantity.data,
      ticketsAvailable=form.ticketQuantity.data)
    # add the object to the db session
    db.session.add(event)
    # commit to the database
    db.session.commit()
    print('Successfully created new event', 'success')
    #Always end with redirect when form is valid
    return redirect(url_for('main.index'))
  return render_template('events/create.html', form=form)


def check_upload_file(form):
  #get file data from form  
  fp=form.eventimage.data
  filename=fp.filename
  #get the current path of the module file… store image file relative to this path  
  BASE_PATH=os.path.dirname(__file__)
  #upload file location – directory of this file/static/image
  upload_path=os.path.join(BASE_PATH,'static/image', filename)
  #store relative path in DB as image location in HTML is relative
  db_upload_path='/static/image/' + str(secure_filename(filename))
  #save the file and return the db upload path  
  fp.save(upload_path)
  return db_upload_path



@bp.route('/<event>/comment', methods = ['GET', 'POST'])  
@login_required
def comment(event):  
    form = CommentForm()  
    
    event_obj = Event.query.filter_by(eventid=event).first()  
    if form.validate_on_submit():  
      #read the comment from the form
      comment = Comment(comment=form.text.data,  
                        event=event_obj,
                        user=current_user) 
      #here the back-referencing works - comment.destination is set
      # and the link is created
      db.session.add(comment) 
      db.session.commit() 

       
      print('Your comment has been added', 'success') 
    # using redirect sends a GET request to event.show
    return redirect(url_for('event.show', id=event))