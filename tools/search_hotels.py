import requests
import os
from search_place import search_place
from dotenv import load_dotenv
from crewai.tools import tool


# load .env to environment
load_dotenv()
api_key = os.getenv("X-Goog-Api-Key")
GOOGLE_HOTELS_BASE_URL = os.getenv("GOOGLE_HOTELS_BASE_URL")
# place_details = search_place('BLR')

# latitude = place_details[0]["latitude"]
# longitude = place_details[0]["longitude"]

@tool("Hotel details")
def hotels_search(arr_iata: float) -> dict:
    """
    This function returns the list of hotel names around the latitude and langitude coordinates provided
    
    Parameters:
    latitude (float), longitude (float): The latitude and longitude values of the airport iata code

    Returns:
    A list of hotel names
    """
    place_details = search_place(arr_iata)

    latitude = place_details[0]["latitude"]
    longitude = place_details[0]["longitude"]
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': api_key,
        'X-Goog-FieldMask': "places.displayName,places.location"
    }
    body = {
        "includedTypes": ["hotel", "lodging"],
        "maxResultCount": 10,
        "locationRestriction": {
        "circle": {
            "center": {
                "latitude": latitude,
                "longitude": longitude
                },
                "radius": 50000.0
                  }
                               }
            }
    response = requests.post(GOOGLE_HOTELS_BASE_URL, headers= headers, json = body)
    result = response.json()
    hotels = []
    for hotel in result["places"]:
        hotels.append({
            "Hotel Name" : hotel["displayName"]["text"]
        })

    return hotels