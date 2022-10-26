from flask import Blueprint, render_template

bp = Blueprint('event',__name__,url_prefix='/event')

@bp.route('/<eventID>')

def show(eventID):
    return render_template('event/show.html')