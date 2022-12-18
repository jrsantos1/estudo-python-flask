from config import App
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import redirect, url_for

db = App().get_db()
login_manager = App().login_manager

@login_manager.user_loader
def get_user(user_id):
    return Usuario.query.filter_by(id=user_id).first()

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('login'))

def get_user(user_id):
    return Usuario.query.filter_by(id=user_id).first()

class Usuario(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True) 
    usuario = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(50), nullable=False)   
    
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = generate_password_hash(senha)
    
    def verify_password(self, senha):
        return check_password_hash(self.senha, senha)