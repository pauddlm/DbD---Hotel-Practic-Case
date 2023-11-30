import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def df_clean_null_id(df):
    #Function that will clean unnecessary data from the dataframe.

    #If we do not know the user id, we do not want the register. Inplace used to modify the original df. 
    df.dropna(subset=['agent'], inplace=True)
    #Parse from double to int.
    df['agent'] = df['agent'].astype(int)
    return df
