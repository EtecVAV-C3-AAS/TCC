
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from ..extensoes import db, login_manager

class Aluno(UserMixin, db.Model):
    __tablename__ = "alunos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    senha_hash = db.Column(db.String(200), nullable=False)
    progresso = db.relationship("Progresso", backref="aluno", lazy=True)
    def definir_senha(self, senha_plana: str) -> None:
        self.senha_hash = generate_password_hash(senha_plana)
    def verificar_senha(self, senha_plana: str) -> bool:
        return check_password_hash(self.senha_hash, senha_plana)

class Progresso(db.Model):
    __tablename__ = "progresso"
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey("alunos.id"), nullable=False)
    materia = db.Column(db.String(60), nullable=False)
    percentual = db.Column(db.Float, default=0.0)
    acertos = db.Column(db.Integer, default=0)
    total = db.Column(db.Integer, default=0)
    atualizado_em = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    __table_args__ = (db.UniqueConstraint("aluno_id", "materia", name="uq_aluno_materia"),)

@login_manager.user_loader
def carregar_aluno(aluno_id):
    return Aluno.query.get(int(aluno_id))
