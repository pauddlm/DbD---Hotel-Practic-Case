from adapters import ApiHotelAdapter, CsvAdapter, SQLiteAdapter, GenderApiAdapter
from infraestructure import SQLiteInfraestructure
from app import DFTransform, UserHotelTransform
import pandas
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

#Retrieving API hotel info
response = ApiHotelAdapter.api_call_hotel()
#Adding first names to the API hotel info
guests_names, response = UserHotelTransform.addUserFirstName(response)
#Retrieving API gender info
gender_response = GenderApiAdapter.api_call_gender(response, guests_names)
#Adding gender to the API hotel info
response = UserHotelTransform.addGender(gender_response, response)
logger.info(f"Response with genders: {response}")


hotel_dataframe = CsvAdapter.csv_read()
hotel_dataframe = DFTransform.df_clean_null_id(hotel_dataframe)

#SQLiteInfraestructure.create_infraestructure_sqlite(response)

# Llamada a la función para recuperar todos los datos de dim_users
all_users_data = SQLiteAdapter.select_all_from_dim_users()

# Imprimir los resultados
for user_data in all_users_data:
    logger.debug(user_data)
