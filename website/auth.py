# This is the root where user can have their view basically
# it means thsi file has the blueprint of our app
# Request is for allowing the http request
# flash is to flash message to user by flask
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

# Below methods=... are actually allowing the http types of request for out page
@auth.route('/login', methods=['Get', 'POST'])
def login():
    # Getting the form data
    # data = request.form
    # print(data)
    return render_template("login.html", text="Testing", user="Tim", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>logout<p>"

@auth.route('/sign-up', methods=['Get', 'POST'])
def sign_up():
    # Taking the information
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        #Creating feedback on user for their registration
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            pasflash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Your account has been created!', category='success')

    return render_template("sign_up.html")