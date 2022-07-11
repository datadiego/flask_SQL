from . import app #desde el modulo balance, importa la aplicacion flask

@app.route("/")
def inicio():
    return "Pagina de inicio"

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    return "Crear movimiento"

@app.route("/modificar", methods=["GET", "POST"])
def actualizar():
    return "Modificar movimiento"

@app.route("/borrar", methods=["GET", "POST"])
def eliminar():
    return "Eliminar un movimiento"