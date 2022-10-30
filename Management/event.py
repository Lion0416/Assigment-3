from asyncio import events
from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from .models import Event
from . import db
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user


bp = Blueprint('event', __name__, url_prefix='/event')

@bp.route('/<eventid>')
def show(id):

    return render_template('destinations/show.html')