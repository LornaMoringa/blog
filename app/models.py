from . import db
from datetime import datetime
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Blogs(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    category = db.Column(db.String(255))
    blog = db.Column(db.String(255))
    date = db.Column(db.DateTime(250), default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id",ondelete='CASCADE'), nullable=False)
    comments = db.relationship('Comments', backref='title', lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def deleteblog(self):
        db.session.delete(self)
        db.session.commit() 

    @classmethod
    def get_blogs(cls):
        blog = Blogs.query.all()
        return blog


    def __repr__(self):
        return f"Blogs {self.blog}','{self.date}')"     


