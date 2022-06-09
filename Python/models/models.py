
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import orm


db = SQLAlchemy()
Base = orm.declarative_base()


class Association(Base):
    __tablename__ = 'association'
    sid = db.Column(db.ForeignKey("student.id"), primary_key=True)
    cid = db.Column(db.ForeignKey("course.id"), primary_key=True)
    course = db.relationship("Course", backref="Association")

    def __init__(self, sid, cid):
        self.sid = sid
        self.cid = cid

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
            'sid': self.sid,
            'cid': self.cid,
        }
    def __repr__(self):
        return f'Student Data: {self.sid} {self.cid}'


class Student(Base):
    __tablename__ ='student'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    gpa = db.Column(db.Float)
    courses = db.relationship("Association", backref="Student")

    def __init__(self, first_name, last_name, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa

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
            'gpa': self.gpa,
        }
    def __repr__(self):
        return f'Student Data: {self.first_name} {self.last_name} {self.gpa}'


class Course(Base):
    __tablename__ ='course'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(128))
    academic_hours = db.Column(db.Integer)
    actual_hours = db.Column(db.Integer)
    tid = db.Column(db.Integer, db.ForeignKey("teacher.id"))

    def __init__(self, name, academic_hours, actual_hours, tid):
        self.name = name
        self.academic_hours = academic_hours
        self.actual_hours = actual_hours
        self.tid = tid

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
            'academic_hours': self.academic_hours,
            'actual_hours': self.actual_hours,
            'tid': self.tid,
        }

    def __repr__(self):
        return f'Course Data: {self.name} {self.academic_hours} {self.actual_hours} {self.tid}'


class Teacher(Base):
    __tablename__ ='teacher'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    course = orm.relationship('Course')

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
        return f'Teacher Data: {self.first_name} {self.last_name}'

