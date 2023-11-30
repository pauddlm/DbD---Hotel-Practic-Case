import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def addUserFirstName(response):
    #Function that retrieves the first name of a person.

    guests_names = []
    for guest in response:
        first_name = guest['name']
        name_parts = first_name.split()
        if 'Mrs.' in name_parts:
            name = name_parts[1]
        else:
            name = name_parts[0]     

        guest['first_name'] = name
        guests_names.append(name)
    
    logger.debug(f"Guests names: {guests_names}")
    logger.debug(f"Response with first names: {response}")
    return guests_names, response
    
def addGender(gender_response, response):
    #Function that adds the gender of a guest to the response.
    gender_info_map = retrieveGender(gender_response)
    logger.info(f"Genderinfomap: {gender_info_map}")
    for guest in response:
        #Let us assume that in this case there are no repeated first names.
        name = guest['first_name']
        if name in gender_info_map:
            guest['gender'] = gender_info_map[name]

    return response

def retrieveGender(gender_response):
    #Function that creates a dictionary with the name and gender of the guests.
    gender_info_map = {}
    for guest in gender_response:
        name = guest['name']
        gender = guest['gender']
        gender_info_map[name] = gender
    
    return gender_info_map