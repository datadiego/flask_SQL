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
            #4.1 obtengo nombres de columna
            # cursor.description devuelve (("nom_col", "val_col"))
            #4.2 pedir todos los datos(registros)
            #4.3 recorrer los resultados
                #4.3.1 crear un diccionario
                    #recorro la lista de los nombres de la columna
                    # para cada columna: nombre+valor
                #4.3.2 guardar en la lista de movimientos
                # obtengo una lista: [{nombre1_col1:val_col1}, {nombre1_col2:val_col2}, ...]  
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

        