
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from . import bp_auth
from ..extensoes import db
from ..models.entidades import Aluno

@bp_auth.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        aluno = Aluno.query.filter_by(nome=nome).first()
        if aluno and aluno.verificar_senha(senha):
            login_user(aluno)
            flash("Login realizado com sucesso!", "success")
            prox = request.args.get("next")
            return redirect(prox or url_for("principal.index"))
        flash("Nome ou senha inválidos.", "danger")
    return render_template("login.html", titulo_pagina="Entrar")

@bp_auth.route("/registro", methods=["GET","POST"])
def registro():
    if request.method == "POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        if not nome or not senha:
            flash("Preencha todos os campos.", "warning")
            return render_template("registro.html", titulo_pagina="Criar conta")
        if Aluno.query.filter_by(nome=nome).first():
            flash("Este nome já está em uso.", "warning")
            return render_template("registro.html", titulo_pagina="Criar conta")
        novo = Aluno(nome=nome); novo.definir_senha(senha)
        db.session.add(novo); db.session.commit()
        flash("Conta criada! Faça login.", "success")
        return redirect(url_for("auth.login"))
    return render_template("registro.html", titulo_pagina="Criar conta")

@bp_auth.route("/sair")
@login_required
def sair():
    logout_user()
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for("principal.index"))
