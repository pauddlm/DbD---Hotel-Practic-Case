import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def df_clean(df):
    #Function that will clean unnecessary data from the dataframe.
    #If we do not know the user id, we do not want the register. Inplace used to modify the original df. 
    df.dropna(subset=['agent'], inplace=True)
    df.dropna(subset=['country'], inplace=True)
    #Parse from double to int.
    df['agent'] = df['agent'].astype(int)
    #Change agent to user_id and drop column agent
    df['user_id'] = df['agent']
    df.drop('agent', axis = 1)
    return df
