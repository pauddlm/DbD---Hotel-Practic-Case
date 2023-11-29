from adapters import ApiAdapter
from adapters import CsvAdapter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


response = ApiAdapter.api_call()
hotel_dataframe = CsvAdapter.csv_read()
