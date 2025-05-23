import pyodbc
import psycopg2

def migrar_datos(cursor_sqlserver, cursor_postgresql, consulta_select, plantilla_insert):
    try:
        cursor_sqlserver.execute(consulta_select)
        for fila in cursor_sqlserver.fetchall():
            cursor_postgresql.execute(plantilla_insert, fila)
        print("Migración completada correctamente.")
    except Exception as e:
        print("Error durante la migración:", e)
        raise

# Conexión a SQL Server
conn_sql = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=PC127\SQLEXPRESS,61061;DATABASE=servi_erp;UID=sa;PWD=Clave01.")
cursor_sql = conn_sql.cursor()

# Conexión a PostgreSQL
conn_pg = psycopg2.connect("host=localhost dbname=servi_erp user=postgres password=Clave01.")
cursor_pg = conn_pg.cursor()


# Migrar Clientes
sql_select = "SELECT nitced, apl1, apl2, nom1, nombre FROM cliente"
sql_insert = """
INSERT INTO cliente (nitced, apl1, apl2, nom1,nombre)
VALUES (%s, %s, %s, %s, %s)
"""


# Llamar función para migrar datos
migrar_datos(cursor_sql, cursor_pg, sql_select, sql_insert)

# Confirmar y cerrar conexiones
conn_pg.commit()
cursor_sql.close()
conn_sql.close()
cursor_pg.close()
conn_pg.close()
