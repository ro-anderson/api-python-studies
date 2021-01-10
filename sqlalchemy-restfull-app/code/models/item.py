
import sqlite3
from db import db
#from flask_restful import Resource, reqparse
#from flask_jwt import jwt_required

class ItemModel(db.Model):

    __tablename__ ='items'


    # told to alchemy that db must have only this 3 columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {"name": self.name, "price": self.price}
 
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # select * from items where name=name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

