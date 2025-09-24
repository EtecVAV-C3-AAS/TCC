
from flask import render_template
from flask_login import login_required, current_user
from . import bp_dashboard
from ..models.entidades import Progresso

@bp_dashboard.route("/")
@login_required
def ver_dashboard():
    materias = ["Alfabetização","Matemática","Cores e Formas","Ciências","História e Cidadania"]
    progresso_por_materia = {m: {"percentual":0,"acertos":0,"total":0} for m in materias}
    registros = Progresso.query.filter_by(aluno_id=current_user.id).all()
    for reg in registros:
        progresso_por_materia[reg.materia] = {"percentual": reg.percentual, "acertos": reg.acertos, "total": reg.total}
    return render_template("dashboard.html", titulo_pagina="Meu Progresso", progresso=progresso_por_materia)
