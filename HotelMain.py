from adapters import ApiHotelAdapter, CsvAdapter, SQLiteAdapter
from infraestructure import SQLiteInfraestructure
from app import DFClean, UserHotelClean
import pandas
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


response = ApiHotelAdapter.api_call_hotel()
response = UserHotelClean.getUserName(response)

hotel_dataframe = CsvAdapter.csv_read()
hotel_dataframe = DFClean.df_clean_null_id(hotel_dataframe)

#SQLiteInfraestructure.create_infraestructure_sqlite(response)

# Llamada a la función para recuperar todos los datos de dim_users
all_users_data = SQLiteAdapter.select_all_from_dim_users()

# Imprimir los resultados
for user_data in all_users_data:
    logger.info(user_data)
