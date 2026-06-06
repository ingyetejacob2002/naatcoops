from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    pf_number = db.Column(db.String(100), unique=True, nullable=False)

    full_name = db.Column(db.String(200), nullable=False)

    email = db.Column(db.String(200), unique=True, nullable=False)

    password_hash = db.Column(db.String(255))

    role = db.Column(db.String(20), default='member')

    approved = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    savings = db.relationship('Savings', backref='member', lazy=True)

    loans = db.relationship('Loan', backref='member', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
class Savings(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    amount = db.Column(db.Float, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    amount = db.Column(db.Float, nullable=False)

    duration = db.Column(db.String(100))

    reason = db.Column(db.Text)

    status = db.Column(db.String(20), default='Pending')

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200))

    message = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


