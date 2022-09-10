# This is the root where user can have their view basically
# it means thsi file has the blueprint of our app
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# Basically this function will run when we go to the route '/'
@views.route('/')
def home():
    return render_template("home.html")