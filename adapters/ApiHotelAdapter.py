import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def api_call_hotel():
    #Function that calls an external API and retrieves the data in the given endpoint
    #Endpoint url
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    if response.status_code == 200:
        users_info = response.json()
        logger.debug(f"Response: {users_info}")
        return users_info
    else:
        error_message = f"The API call to jsonplaceholder.typicode.com failed. Response status code: {response.status_code}"
        raise Exception(error_message)