import sqlite3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def select(query):
    # Conectar a la base de datos
    conexion = sqlite3.connect('dbd_hotel_resorts.db')
    cursor = conexion.cursor()

    # Ejecutar la consulta SELECT *
    cursor.execute(query)

    # Recuperar todos los resultados
    results = cursor.fetchall()

    # Cerrar la conexión
    conexion.close()

    for user_data in results:
        logger.info(user_data)

    # Devolver los resultados
    return results

def drop_table_dim_users():
    # Conectar a la base de datos
    conexion = sqlite3.connect('dbd_hotel_resorts.db')
    cursor = conexion.cursor()

    # Ejecutar la consulta DROP TABLE
    cursor.execute('DROP TABLE dim_users;')

    # Recuperar todos los resultados
    results = cursor.fetchall()

    # Cerrar la conexión
    conexion.close()

    # Devolver los resultados
    return results