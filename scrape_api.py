# Data to extract from high level place object
place_keys = [
    'place_id',
    'lon',
    'lat',
    'display_name',
    'type'
]

# Data to extract from address sub-object
address_keys = [
    'city',
    'state',
    'state',
    'postcode',
    'country',
    'country_code'
]

def build_raw_row_from_result(response: dict, central_id: str) -> dict:

    """
    Scrapes a set of values from an API response. 

    Parameters:
    response (dict): Response from the API request (Basic search).
    central_id (str): Central ID to track the row.

    Returns:
    dict: The sum of the two numbers.
    """

    final_data = dict()
    final_data['central_id'] = central_id

    # Get result with highest importance
    place_data = max(response, key=lambda x: x['importance'])

    # Get the high level place info
    for place_key in place_keys:
        if place_key not in place_data.keys():
            final_data[place_key] = None
        else:
            final_data[place_key] = place_data[place_key]

    # Get the address specific info
    if 'address' in place_data.keys():
        address_data = place_data['address']
        for address_key in address_keys:
            if address_key not in address_data.keys():
                final_data[address_key] = None
            else:
                final_data[address_key] = address_data[address_key]
    else:
        for key in address_keys:
            final_data[key] = None

    return final_data