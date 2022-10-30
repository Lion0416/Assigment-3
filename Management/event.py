from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from .models import Event
from . import db, app
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user