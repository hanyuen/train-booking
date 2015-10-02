from database import db

class Train(db.Model):
    __tablename__ = "trains"

    id = db.Column(db.Integer, primary_key=True)
    train_id = db.Column(db.String, nullable=False)
    fromCity = db.Column(db.String, nullable=False)
    toCity = db.Column(db.String, nullable=False)
    size = db.Column(db.Integer, nullable=True)



    def __repr__(self):
        return '<train_id %r>' % self.train_id
