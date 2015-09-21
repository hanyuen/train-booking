from database import db
#from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mytrains.db'
# db = SQLAlchemy(app)

class Train(db.Model):
    __tablename__ = "trains"

    id = db.Column(db.Integer, primary_key=True)
    train_id = db.Column(db.String, nullable=False)
    fromCity = db.Column(db.String, nullable=False)
    toCity = db.Column(db.String, nullable=False)
    size = db.Column(db.Integer, nullable=True)

    def __init__(self, train_id, fromCity, toCity, size):
        self.train_id = train_id
        self.fromCity = fromCity
        self.toCity = toCity
        self.size = size

    def __repr__(self):
        return '<train_id %r>' % self.train_id
