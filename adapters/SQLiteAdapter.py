import sqlite3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def select(query):
    # Connect to the database
    conexion = sqlite3.connect('dbd_hotel_resorts.db')
    cursor = conexion.cursor()

    # Execute the query
    cursor.execute(query)

    # Retrieve the results
    results = cursor.fetchall()

    # Close the connexion
    conexion.close()

    #Log the results
    for user_data in results:
        logger.info(user_data)

    return results