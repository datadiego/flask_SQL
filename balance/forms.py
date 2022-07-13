from sqlite3 import Date
from flask_wtf import FlaskForm
from wtforms import HiddenField, DateField, StringField, RadioField, DecimalField, SubmitField

class MovimientosForm(FlaskForm):
    id = HiddenField()
    fecha = DateField("Fecha")
    concepto = StringField("Concepto")
    tipo = RadioField(choices=[("I", "Ingreso"), ("G", "Gasto")])
    cantidad = DecimalField("Cantidad", places=2)

    submit = SubmitField("Guardar")

