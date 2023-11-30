import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def api_call_gender(response):
    #Function that calls an external API and retrieves the gender given de name.
    return