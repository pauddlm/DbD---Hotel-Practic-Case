import sqlite3

def select_all_from_dim_users():
    # Conectar a la base de datos
    conexion = sqlite3.connect('dbd_hotel_resorts.db')
    cursor = conexion.cursor()

    # Ejecutar la consulta SELECT *
    cursor.execute('SELECT * FROM dim_users WHERE user_id < 5')

    # Recuperar todos los resultados
    results = cursor.fetchall()

    # Cerrar la conexión
    conexion.close()

    # Devolver los resultados
    return results
