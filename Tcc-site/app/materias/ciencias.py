
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..extensoes import db
from ..models.entidades import Progresso

bp_ciencias = Blueprint("ciencias", __name__, template_folder="../templates", url_prefix="/ciencias")

@bp_ciencias.route("/")
@login_required
def atividade():
    return render_template("atividade_ciencias.html", titulo_pagina="Ciências")

@bp_ciencias.route("/enviar", methods=["POST"])
@login_required
def enviar():
    total = 3; acertos = 0
    corretas = {"q1":"a","q2":"b","q3":"a"}
    for k,v in corretas.items():
        if request.form.get(k) == v: acertos += 1
    percentual = round((acertos/total)*100, 2)
    _salvar("Ciências", acertos, total, percentual)
    flash(f"Você fez {acertos}/{total} ({percentual}%).", "info")
    return redirect(url_for("ciencias.atividade"))

def _salvar(materia, acertos, total, percentual):
    r = Progresso.query.filter_by(aluno_id=current_user.id, materia=materia).first()
    if not r: r = Progresso(aluno_id=current_user.id, materia=materia); db.session.add(r)
    r.acertos, r.total, r.percentual = acertos, total, percentual
    db.session.commit()
