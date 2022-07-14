from flask_wtf import FlaskForm
from wtforms import HiddenField, DateField, StringField, RadioField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length
class MovimientosForm(FlaskForm):
    id = HiddenField()
    fecha = DateField("Fecha", validators=[DataRequired("Debes introducir una fecha")])
    concepto = StringField("Concepto", validators=[
        DataRequired("Debes introducir un concepto"),
        Length(3, 25, "Debe tener entre 3 y 25 caracteres")    
    ])
    tipo = RadioField(choices=[("I", "Ingreso"), ("G", "Gasto")],
        validator=[DataRequired("¿Es un gasto o un tipo?")]
    )
    cantidad = FloatField("Cantidad", validators=[DataRequired("Debes escribir una cantidad")])

    submit = SubmitField("Guardar", render_kw={"class":"blue-button"})

