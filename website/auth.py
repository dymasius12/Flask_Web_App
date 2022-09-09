# This is the root where user can have their view basically
# it means thsi file has the blueprint of our app
from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login<p>"

@auth.route('/logout')
def logout():
    return "<p>logout<p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up<p>"