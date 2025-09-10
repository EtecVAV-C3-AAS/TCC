
from flask import Flask
from .extensoes import db, login_manager
from .config import Configuracao
from .auth.rotas import bp_auth
from .principal.rotas import bp_principal
from .dashboard.rotas import bp_dashboard
from .materias.alfabetizacao import bp_alfabetizacao
from .materias.matematica import bp_matematica
from .materias.cores_formas import bp_cores_formas
from .materias.ciencias import bp_ciencias
from .materias.historia_cidadania import bp_historia

def criar_app():
    app = Flask(__name__)
    app.config.from_object(Configuracao)
    db.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        from .models.entidades import Aluno, Progresso  # noqa
        db.create_all()
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_principal)
    app.register_blueprint(bp_dashboard, url_prefix="/dashboard")
    app.register_blueprint(bp_alfabetizacao, url_prefix="/materias/alfabetizacao")
    app.register_blueprint(bp_matematica, url_prefix="/materias/matematica")
    app.register_blueprint(bp_cores_formas, url_prefix="/materias/cores-formas")
    app.register_blueprint(bp_ciencias, url_prefix="/materias/ciencias")
    app.register_blueprint(bp_historia, url_prefix="/materias/historia-cidadania")
    return app
