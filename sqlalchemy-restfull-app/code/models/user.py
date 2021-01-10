import sqlite3
from db import db

class UserModel(db.Model):

    __tablename__ ='users'

    # told to alchemy that db must have only this 3 columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        '''
        by username retrieve User.
        '''
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        '''
        by _id retrieve User.
        '''
        return cls.query.filter_by(id=_id).first()

