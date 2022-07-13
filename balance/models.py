import sqlite3

class DBManager:
    def __init__(self, ruta):
        self.ruta = ruta
    
    def consultaSQL(self, consulta):
        #1 conectar con la base de datos
        conexion = sqlite3.connect(self.ruta)

        #2 abrir un cursor
        cursor = conexion.cursor()

        #3 ejecutar consulta SQL (select, delete...)
        cursor.execute(consulta)

        #4 tratar los datos

        self.movimientos = []
        nombres_columnas = []

        for desc_columna in cursor.description:
            #devuelve como esta definida nuestra tabla
            nombres_columnas.append(desc_columna[0])
        #nombres_columnas ahora es ["id", "fecha", "concepto", "tipo", "cantidad"]
        datos = cursor.fetchall()

        for dato in datos:
            movimiento = {}
            indice = 0
            for nombre in nombres_columnas:
                movimiento[nombre] = dato[indice]
                indice += 1
            self.movimientos.append(movimiento)

        conexion.close()
        return self.movimientos

    def borrar(self, id):
        consulta = "DELETE from movimientos WHERE id=?"
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        resultado = False
        try:
            cursor.execute(consulta, (id,)) #DELETE from movimientos WHERE id=3
            conexion.commit()
            resultado = True
        except:
            conexion.rollback()
        conexion.close()   
        return resultado

        