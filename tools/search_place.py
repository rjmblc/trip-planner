import requests

import os
from dotenv import load_dotenv
from crewai.tools import tool

# load .env to environment
load_dotenv()

api_key = os.getenv("X-Goog-Api-Key")
GOOGLE_PLACES_BASE_URL = os.getenv("GOOGLE_PLACES_BASE_URL")

@tool("Aiport details and it's geogrpahical coordinates")
def search_place(arr_iata: str) -> dict:
    """
    This function returns the list of airport name, its geographical co-ordinates like latitude and longitude
    
    Parameters:
    arr_iata (str): The iata codes for the arrival airports. (eg: MAA, BLR) 

    Returns:
    A list containing airport fullname, airport latitude & longitude
    """
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': api_key,
        'X-Goog-FieldMask': "places.displayName,places.location"
    }
    body = {
        "textQuery": f"{arr_iata} Airport" 
    }
    response = requests.post(GOOGLE_PLACES_BASE_URL,headers=headers,json=body)
    output = response.json()
    place_list = []
    for details in output["places"]:
        place_list.append({
            "latitude" : details["location"]["latitude"],
            "longitude" : details["location"]["longitude"],
            "airport name" : details["displayName"]["text"]
        })
    
    return place_list
