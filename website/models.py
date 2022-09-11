# We are going to have the database model for our app
# From this package import db
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # This is how to associate different info to some others, the relationship
    # setup the foreign key
    # foreign key is small no caps
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



class User(db.Model, UserMixin):
    # Then we define the colomn we want in the database table
    id = db.Column(db.Integer, primary_key=True)
    # Unique meaning means no other user can have the same value
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # Basically a list that stored all the different notes
    # for relationship is caps
    notes = db.relationship('Note')