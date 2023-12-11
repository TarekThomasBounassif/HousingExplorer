import requests

from api_request_constants import (
    LOC_IQ_KEY,
    BASIC_SEARCH_URL,
    NEARBY_SEARCH_EU,
    NEARBY_SEARCH_US
)

class LocationIqRequester:

    def __init__(self) -> None:
        self.total_api_call_count = 0
        self.successful_api_calls = 0
        self.error_api_calls = 0
        self.basic_search_url = BASIC_SEARCH_URL
        self.nearby_us = NEARBY_SEARCH_US
        self.nearby_eu = NEARBY_SEARCH_EU

    def location_iq_api_call(self, api_url: str, params: dict) -> list:
        
        try:
            self.total_api_call_count += 1
            params["key"] = LOC_IQ_KEY
            response = requests.get(api_url, params=params)
            
            if response.status_code == 200:
                self.successful_api_calls += 1
                return response.json()
            else:
                self.error_api_calls += 1
                return response.raise_for_status()

        except requests.exceptions.RequestException as e:
            self.error_api_calls += 1
            raise e

    def get_location_details(self, input_address: str) -> list:

        params = {
            "q": input_address,
            "format": "json",
            "normalizecity": 1,
            "normalizeaddress": 1,
            "dedupe": 1,
            "addressdetails": 1
        }

        return self.location_iq_api_call(self.basic_search_url, params)

