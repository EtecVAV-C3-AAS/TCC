
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..extensoes import db
from ..models.entidades import Progresso

bp_matematica = Blueprint("matematica", __name__, template_folder="../templates", url_prefix="/matematica")

@bp_matematica.route("/")
@login_required
def atividade():
    return render_template("atividade_matematica.html", titulo_pagina="Matemática Básica")

@bp_matematica.route("/enviar", methods=["POST"])
@login_required
def enviar():
    total = 3; acertos = 0
    corretas = {"q1":"c","q2":"a","q3":"b"}
    for k,v in corretas.items():
        if request.form.get(k) == v: acertos += 1
    percentual = round((acertos/total)*100, 2)
    _salvar("Matemática", acertos, total, percentual)
    flash(f"Resultado: {acertos}/{total} ({percentual}%).", "info")
    return redirect(url_for("matematica.atividade"))

def _salvar(materia, acertos, total, percentual):
    r = Progresso.query.filter_by(aluno_id=current_user.id, materia=materia).first()
    if not r: r = Progresso(aluno_id=current_user.id, materia=materia); db.session.add(r)
    r.acertos, r.total, r.percentual = acertos, total, percentual
    db.session.commit()
