
from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from ..extensoes import db
from ..models.entidades import Progresso

bp_cores_formas = Blueprint("cores_formas", __name__, template_folder="../templates", url_prefix="/cores-formas")

@bp_cores_formas.route("/")
@login_required
def atividade():
    return render_template("atividade_cores_formas.html", titulo_pagina="Cores e Formas")

@bp_cores_formas.route("/resultado", methods=["POST"])
@login_required
def resultado():
    dados = request.get_json(force=True)
    acertos = int(dados.get("acertos", 0)); total = int(dados.get("total", 0))
    percentual = round((acertos/total)*100, 2) if total else 0
    r = Progresso.query.filter_by(aluno_id=current_user.id, materia="Cores e Formas").first()
    if not r: r = Progresso(aluno_id=current_user.id, materia="Cores e Formas"); db.session.add(r)
    r.acertos, r.total, r.percentual = acertos, total, percentual
    db.session.commit()
    return jsonify({"ok": True, "percentual": percentual})
