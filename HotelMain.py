from adapters import ApiHotelAdapter, CsvAdapter, GenderApiAdapter
from infraestructure import SQLiteInfraestructure
from app import DFTransform, UserHotelTransform
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

###### EXTERNAL API ETL ######
#Retrieving API hotel info
response = ApiHotelAdapter.api_call_hotel()
#Adding first names to the API hotel info
guests_names, response = UserHotelTransform.addUserFirstName(response)
#Retrieving API gender info
gender_response = GenderApiAdapter.api_call_gender(response, guests_names)
#Adding gender to the API hotel info
response = UserHotelTransform.addGender(gender_response, response)
#Generating SQLite table with the enriched response
SQLiteInfraestructure.create_infraestructure_sqlite_hotel_api(response)


###### CSV ETL ######
#Reading CSV and transforming it into a pandas dataframe 
hotel_dataframe = CsvAdapter.csv_read()
#Applying some transformations to the dataframe
hotel_dataframe = DFTransform.df_clean(hotel_dataframe)
#Generating SQLite table with the cleaned dataframe
SQLiteInfraestructure.create_infraestructure_sqlite_hotel_csv(hotel_dataframe)


