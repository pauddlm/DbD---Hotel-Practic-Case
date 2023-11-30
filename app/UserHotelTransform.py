import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def getUserName(response):
    #Function that retrieves the first name of a person.

    for guest in response:
        first_name = guest['name']
        name_parts = first_name.split()
        if len(name_parts) == 2:
            name = name_parts[0]
        if len(name_parts) == 3:
            name = name_parts[1]
        guest['first_name'] = name
    
    logger.info(f"Response with first names: {response}")
    return response
    