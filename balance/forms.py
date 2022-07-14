from flask_wtf import FlaskForm
from wtforms import HiddenField, DateField, StringField, RadioField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length
class MovimientosForm(FlaskForm):
    id = HiddenField()
    fecha = DateField("Fecha", validators=[DataRequired("Debes introducir una fecha")])
    concepto = StringField("Concepto", validators=[DataRequired()])
    tipo = RadioField(choices=[("I", "Ingreso"), ("G", "Gasto")])
    cantidad = FloatField("Cantidad")

    submit = SubmitField("Guardar", render_kw={"class":"blue-button"})

