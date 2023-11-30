import csv
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def csv_read():
    #Function that reads a CSV and converts it into a pandas dataframe
    
    try:
        with open(r"D:\VSCode\DbD---Hotel-Practic-Case\reservasHotel.csv", 'r', newline='') as csv_file:
            # Read the CSV and create a dataframe
            df = pd.read_csv(csv_file, delimiter=';')
        logger.debug(f"CSV read and converted to dataframe correctly.")
        return df
    
    except Exception as e:
        logger.error(f"Error when reading and converting the dataframe: {e}")
        raise
