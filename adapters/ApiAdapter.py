import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def api_call():
    #Function that calls an external API and retrieves the data in the given endpoint.
    
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        users_info = response.json()
        logger.debug(f"Response: {users_info}")
        return users_info
    else:
        error_message = f"The API call failed. Response status code: {response.status_code}"
        raise Exception(error_message)