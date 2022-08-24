from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    namaLengkap = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(60))
    orders = db.relationship('Order')

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    durasiSewa = db.Column(db.Integer)
    totalBiaya = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    lokasi_id = db.Column(db.Integer, db.ForeignKey('lokasi.id')) 

class Lokasi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namaLokasi= db.Column(db.String(100), unique=True)
    sewaPerJam = db.Column(db.Integer)
    orders = db.relationship('Order')