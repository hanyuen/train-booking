__author__ = 'hanyuen'


from app import db
from models import Train

db.create_all()

db.session.add(Train('A1', 'aylmer', 'ottawa', 700))
db.session.add(Train('B2', 'ottawa', 'montreal', 300))
db.session.add(Train('C32', 'toronto', 'montreal', 500))
db.session.add(Train('D42', 'toronto', 'Vancouver', 1200))

db.session.commit()