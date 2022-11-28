from exts import db
from datetime import datetime



# the event database
class EventModel(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    module_title = db.Column(db.String(200), nullable=False)
    assessment_title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text,nullable = False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    due_year = db.Column(db.Integer, nullable = False)
    due_month = db.Column(db.Integer, nullable=False)
    due_day = db.Column(db.Integer, nullable = False)
    status = db.Column(db.String(200), nullable=False)
    trash = db.Column(db.String(200), nullable=False)
    important = db.Column(db.String(200), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship("UserModel", backref="event")





# the email database
class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(100),nullable =False,unique=True)
    captcha = db.Column(db.String(10),nullable = False)
    create_time = db.Column(db.DateTime,default=datetime.now)


# the user information
class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable =False,unique=True)
    email = db.Column(db.String(100),nullable =False,unique=True)
    password = db.Column(db.String(200),nullable =False)
    jointime = db.Column(db.DateTime,default=datetime.now)







