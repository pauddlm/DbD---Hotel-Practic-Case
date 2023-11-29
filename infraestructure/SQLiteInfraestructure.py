import sqlite3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def create_infraestructure_sqlite(users_info):
    # Creating a sqlite database
    conexion = sqlite3.connect('dbd_hotel_resorts.db')
    cursor = conexion.cursor()

    # Creating a SQLite table for the users information of the API
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dim_users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            email TEXT,
            phone TEXT,
            company_name TEXT,
            zipcode TEXT
        )
    ''')       

    #Populating the table with the users information of the API 
    for user in users_info:
        cursor.execute('''
            INSERT INTO dim_users (user_id, username, email, phone, company_name, zipcode)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user['id'], 
              user['username'], 
              user['email'], 
              user['phone'], 
              user['company']['name'], 
              user['address']['zipcode']))        

    #Commit the changes and confirm the connexion
    conexion.commit()
    conexion.close()
 
