import pyodbc
import psycopg2

# 🔗 Conexión a SQL Server Express
sql_server_conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=PC127\SQLEXPRESS,61061;'
    'DATABASE=servi_erp;'
    'UID=sa;'
    'PWD=Clave01.'
)
sql_cursor = sql_server_conn.cursor()

# 🔗 Conexión a PostgreSQL
pg_conn = psycopg2.connect(
    dbname='servi_erp',
    user='postgres',
    password='Clave01.',
    host='localhost',
    port='5432'
)
pg_cursor = pg_conn.cursor()

# 👇 Consulta datos desde SQL Server
#sql_cursor.execute("SELECT nitced, nombre, email FROM cliente")
sql_cursor.execute("SELECT agencia,numfac,nitced from factura")
rows = sql_cursor.fetchall()

# 👇 Inserta en PostgreSQL
for row in rows:
    pg_cursor.execute(
#        "INSERT INTO cliente (nitced, nombre, email) VALUES (%s, %s, %s)",
        "INSERT INTO factura (agencia,numfac,nitced) VALUES (%s, %s, %s)",
        (row.agencia, row.numfac, row.nitced)
#        (row.nitced, row.nombre, row.email)
    )

# 💾 Confirmar cambios
pg_conn.commit()

# 🔚 Cerrar conexiones
sql_cursor.close()
sql_server_conn.close()
pg_cursor.close()
pg_conn.close()

print("Migración completada exitosamente.")

#primero tenemos que descargar el paquete 
#pip install pyodbc psycopg2
