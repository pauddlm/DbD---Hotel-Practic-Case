import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def api_call_gender(response, guests_names):
    #Function that calls an external API and retrieves the gender given a first name

    # Endpoint url
    url = "https://api.genderize.io/"
    # Parameters of the requests with the names
    params = {"name[]": guests_names}
    genderize_response = requests.get(url, params=params)
    if genderize_response.status_code == 200:
        gender_response = genderize_response.json()
        #Let us know that all the names are registered in the API to avoid some checks :) 
        logger.debug(f"Gender information of the guests: {gender_response}")
        return gender_response
    else:
        error_message = f"The API call to genderize.io failed. Response status code: {genderize_response.status_code}"
        raise Exception(error_message)