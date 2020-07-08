import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__)) # __file__ = name of actual file i.e basic.py

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

###################################################################

#creating database model

class Puppy(db.Model):

    __tablename__ = 'puppies'

    #creating columns of table

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def __repr__(self):
        return f"Puppy {self.name} has {self.age} old"

