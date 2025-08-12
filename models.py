import uuid
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import foreign
db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))  
    uuid = db.Column(db.String(36), unique=True, default=lambda: str(uuid.uuid4()))  
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean, default=False)

    students = db.relationship('Student', backref='user', lazy=True)
    payments = db.relationship('Payment', backref='user', lazy=True)
    students = db.relationship('Student', backref='user', lazy=True, cascade="all, delete-orphan")
    payments = db.relationship('Payment', backref='user', lazy=True, cascade="all, delete-orphan")
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll = db.Column(db.String(50), nullable=False)
    batch = db.Column(db.String(50))
    name = db.Column(db.String(100))
    college = db.Column(db.String(100))
    student_number = db.Column(db.String(20))
    guardian_number = db.Column(db.String(20))
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll = db.Column(db.String(50))
    name = db.Column(db.String(100))
    batch = db.Column(db.String(50))
    date = db.Column(db.String(50))
    course = db.Column(db.String(100))
    total_payment = db.Column(db.Integer)
    previous_payment = db.Column(db.Integer)
    discount = db.Column(db.Integer)
    due = db.Column(db.Integer)
    status = db.Column(db.String(20))
    reference = db.Column(db.String(100))
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)

    student = db.relationship(
        'Student',
        primaryjoin="Payment.roll == foreign(Student.roll)",
        viewonly=True,
        uselist=False  # ✅ এটা দাও
    )

class NewPayment(db.Model):
    __tablename__ = 'new_payments'

    id = db.Column(db.Integer, primary_key=True)
    roll = db.Column(db.String(50), nullable=False)
    new_payment = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(50), nullable=True)
    memo_no = db.Column(db.String(50), nullable=True)
    receipt_no = db.Column(db.String(50), nullable=True)
    course = db.Column(db.String(100), nullable=True)
    user_id = db.Column(db.String(100), nullable=False)

    # Relationship with Student
    student = db.relationship(
    'Student',
    primaryjoin="foreign(NewPayment.roll) == Student.roll",
    viewonly=True,
    uselist=False
    )
    def __repr__(self):
        return f'<NewPayment Roll: {self.roll}, Amount: {self.new_payment}>'
