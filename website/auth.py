# This is the root where user can have their view basically
# it means thsi file has the blueprint of our app
# Request is for allowing the http request
# flash is to flash message to user by flask
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
# for security reason, we use werkzeug for password hashing
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


auth = Blueprint('auth', __name__)

# Below methods=... are actually allowing the http types of request for out page
@auth.route('/login', methods=['Get', 'POST'])
def login():
    # Getting the form data
    # data = request.form
    # print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check whether it is the correct value
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('logged in successfully!', category='success')
            else:
                flash('incorrect password, try again.', category='error')
        else:
            flash('email does not exist!', category='error')
    return render_template("login.html", text="Testing", user="Tim", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>logout<p>"

@auth.route('/sign-up', methods=['Get', 'POST'])
def sign_up():
    # Taking the information
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exist!', category='error')
        #Creating feedback on user for their registration
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            pasflash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Now we create the user
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Your account has been created!', category='success')
            # Then redirect the user to the homepage of the website
            # why i put the url_for is if you changed the root it still works. views is the blueprint name 
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")