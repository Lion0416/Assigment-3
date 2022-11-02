from flask import Blueprint, render_template
from .models import Type,States
from .models import Event,Comment
from .forms import EventForm,CommentForm

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    form = EventForm()
    form.event_type.choices = [(type.typeid,type.type) for type in Type.query.all()]
    form.event_state.choices = [(states.statesid,states.states) for states in States.query.all()]




    return render_template('index.html',form=form)