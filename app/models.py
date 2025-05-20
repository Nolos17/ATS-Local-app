from . import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


class OfertaLaboral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    ciudad = db.Column(db.String(100), nullable=False)
    objetivo = db.Column(db.Text, nullable=False)
    requisitos = db.Column(db.Text, nullable=False)
    habilidades = db.Column(db.Text, nullable=False)  # separadas por comas
    correo_contacto = db.Column(db.String(150), nullable=False)
    asunto_correo = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f'<Oferta {self.titulo}>'
    


