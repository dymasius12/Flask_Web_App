# This is the root where user can have their view basically
# it means thsi file has the blueprint of our app
from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

# Basically this function will run when we go to the route '/'
@views.route('/')
# so now you cannot get to the homepage unless you login
@login_required
def home():
    return render_template("home.html")