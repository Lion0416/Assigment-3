from cmath import e
from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 

bp = Blueprint('error', __name__)

@bp.errorhandler(404)
def hander_404_error(e):
    print(e)
    return render_template('404.html')

@bp.errorhandler(500)
def hander_500_error(e):
    print(e)
    return render_template('500.html')