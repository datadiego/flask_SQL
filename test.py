from balance.models import DBManager
manager = DBManager("./data/balance.db")
manager.ruta
sql = "SELECT id, fecha, concepto, tipo, cantidad	FROM movimientos order by cantidad DESC"
manager.consultaSQL(sql)
print(manager.movimientos)