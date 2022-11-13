from flask import Blueprint, render_template
from .models import Type,States
from .models import Event,Comment,Type,States
from .forms import EventForm,CommentForm
from.import db
from sqlalchemy.orm import sessionmaker



mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    
    #events = Event.query.all()
    events = db.session.query(Event, Type, States).select_from(Event).join(Type).join(States).all()
    

    
    
    form = EventForm()
    form.event_type.choices = [(type.typeid,type.type) for type in Type.query.all()]
    form.event_state.choices = [(states.statesid,states.states) for states in States.query.all()]




    return render_template('index.html',events=events,form=form)