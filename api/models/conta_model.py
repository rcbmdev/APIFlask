from api import db

class Conta(db.Model):
    __tablename__='conta'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.Float, nullable=False)