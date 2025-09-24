
from flask import render_template
from . import bp_principal
@bp_principal.route("/")
def index():
    return render_template("index.html", titulo_pagina="EducaFeliz – Início")
