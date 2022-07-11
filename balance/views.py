from . import app #desde el modulo balance, importa la aplicacion flask

@app.route("/")
def inicio():
    return "Pagina de inicio"

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    return "Crear movimiento"

@app.route("/modificar/<int:id>", methods=["GET", "POST"])
def actualizar(id):
    return f"Modificar movimiento con ID:{id}"

@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def eliminar(id):
    return f"Eliminar un movimiento con ID: {id}"