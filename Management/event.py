from flask import Blueprint, render_template

bp = Blueprint('event',__name__,url_prefix='/event')

@bp.route('/<id>')

def show(id):
    return render_template('event/show.html')