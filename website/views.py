# This is the root where user can have their view basically
# it means thsi file has the blueprint of our app
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

# Basically this function will run when we go to the route '/'
@views.route('/', methods=['GET', 'POST'])
# so now you cannot get to the homepage unless you login
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            # Means we are adding the Note to the database
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note is added', category='success')
    # we will be able to reference this current user and check if it is authenticated
    return render_template("home.html", user=current_user)