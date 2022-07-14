from datetime import date

from balance import forms
from . import app #desde el modulo balance, importa la aplicacion flask
from .models import DBManager
from .forms import MovimientosForm
from flask import render_template, request, url_for, redirect

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
        db = DBManager(RUTA)
        movimiento = db.obtener_movimiento_por_id(id)
        movimiento["fecha"] = date.fromisoformat(movimiento["fecha"])
        formulario = MovimientosForm(data=movimiento)
        return render_template("form_movimiento.html", form=formulario, id=id)

    elif request.method == "POST":
        form = MovimientosForm(data=request.form)
        if form.validate():
            db = DBManager(RUTA)
            consulta = "UPDATE movimientos SET fecha=?, concepto=?, tipo=?, cantidad=? WHERE id=?"
            params = (form.fecha.data, form.concepto.data, form.tipo.data, form.cantidad.data, form.id.data)
            resultado = db.consulta_con_parametros(consulta, params)
            if resultado:
                return redirect(url_for("inicio"))
            return render_template("form_movimiento.html", form=form, id=id, errores=["No se ha podido guardar en la base de datos"])
        else:
            return render_template("form_movimiento.html", form=form, id=id, errores=["Ha fallado la validación de los datos"])
        
    

@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def eliminar(id):
    db=DBManager(RUTA)
    consulta = "DELETE from movimientos WHERE id=?"
    #esta_borrado = db.borrar(id)
    params = (id,)
    esta_borrado = db.consulta_con_parametros(consulta, params)
    return render_template("borrar.html", resultado=esta_borrado)