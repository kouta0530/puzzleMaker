from flask_login import UserMixin
from puzzlemaker import db

class User(UserMixin):
    def __init__(self,id):
        self.id = id

    def set_username(self,user_name):
        self.name = user_name
    
    def get_id(self):
        return self.id

class Users(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer,primary_key = True)
    session_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    name = db.Column(db.Text)
    password = db.Column(db.Text)

def init():
    db.create_all()

def get_user_id(session_id):
    user =  Users.query.filter(Users.session_id == session_id).first()
    return user.user_id

def update_session_id(column,session_id):
    column.session_id = session_id
    db.session.add(column)
    db.session.commit()
