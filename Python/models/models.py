
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ ='student'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }
    def __repr__(self):
        return f'Student Name: {self.first_name} {self.last_name}'

class Courses(db.Model):
    __tablename__ ='courses'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128))

    def __init__(self, name):
        self.name = name


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __repr__(self):
        return f'Course Name: {self.name} '
