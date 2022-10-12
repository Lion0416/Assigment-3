from flask import Blueprint, render_template

mainbp = Blueprint('mian', __name__)

@mainbp.route('/')
def index():
    return render_template('index.html')