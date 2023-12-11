import pandas as pd

API_KEYS = pd.read_csv("api_keys.csv")
LOC_IQ_KEY = API_KEYS[API_KEYS['api_key_type'] == 'location_iq']['key'][0]

BASIC_SEARCH_URL = "https://us1.locationiq.com/v1/search.php"
NEARBY_SEARCH_US = "https://us1.locationiq.com/v1/nearby"
NEARBY_SEARCH_EU = "https://eu1.locationiq.com/v1/nearby"