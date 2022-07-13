from balance import forms
from . import app #desde el modulo balance, importa la aplicacion flask
from .models import DBManager
from .forms import MovimientosForm
from flask import render_template, request

RUTA = "data/balance.db"

@app.route("/")
def inicio():
    db = DBManager(RUTA)
    movimientos = db.consultaSQL("SELECT * FROM movimientos")
    return render_template("inicio.html", movs=movimientos)

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    return "Crear movimiento"

@app.route("/modificar/<int:id>", methods=["GET", "POST"])
def actualizar(id):
    if request.method == "GET":
        formulario = MovimientosForm()
        return render_template("form_movimiento.html", form=formulario)
    return f"Modificar movimiento con ID:{id}"

@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def eliminar(id):
    db=DBManager(RUTA)
    esta_borrado = db.borrar(id)
    return render_template("borrar.html", resultado=esta_borrado)