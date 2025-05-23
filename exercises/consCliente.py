import pyodbc
import psycopg2
from datetime import datetime
import time

# Obtener la hora actual (hora1)
hora1 = datetime.now()
print("Hora 1:", hora1)

# 🔗 Conexión a SQL Server Express
sql_server_conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=192.168.50.51;'
    'DATABASE=serviparamo;'
    'UID=sa;'
    'PWD=Clave01.'
)
sql_cursor = sql_server_conn.cursor()

# 🔗 Conexión a PostgreSQL
#pg_conn = psycopg2.connect(
#    dbname='servi_erp',
#    user='postgres',
#    password='Clave01.',
#    host='localhost',
#    port='5432'
#)
#pg_cursor = pg_conn.cursor()

# 👇 Consulta datos desde SQL Server
sql_cursor.execute("select * from com_peda03")
#sql_cursor.execute("SELECT nitced, nombre, email FROM grl_nita01")
#sql_cursor.execute("SELECT agencia,numfac,nitced from factura")
rows = sql_cursor.fetchall()

# 👇 Inserta en PostgreSQL
#for row in rows:
#    pg_cursor.execute(
#        "INSERT INTO cliente (nitced, nombre, email) VALUES (%s, %s, %s)",
#        "INSERT INTO factura (agencia,numfac,nitced) VALUES (%s, %s, %s)",
#      (row.agencia, row.numfac, row.nitced)
#        (row.nitced, row.nombre, row.email)
#    )

# 💾 Confirmar cambios
#pg_conn.commit()

# 🔚 Cerrar conexiones
sql_cursor.close()
sql_server_conn.close()
#pg_cursor.close()
#pg_conn.close()

print("Consulta completada .")
# Obtener la hora actual (hora2)
hora2 = datetime.now()
print("Hora 2:", hora2)

# Calcular diferencia
diferencia = hora2 - hora1

# Mostrar diferencia en formato hh:mm:ss
print("Diferencia:", str(diferencia))

# O como componentes separados
segundos = diferencia.total_seconds()
horas = int(segundos // 3600)
minutos = int((segundos % 3600) // 60)
segundos_restantes = int(segundos % 60)

print(f"Diferencia exacta: {horas} hora(s), {minutos} minuto(s), {segundos_restantes} segundo(s)")

#primero tenemos que descargar el paquete 
#pip install pyodbc psycopg2
