import requests

import os
from dotenv import load_dotenv

# load .env to environment
load_dotenv()

api_key = os.getenv("X-Goog-Api-Key")
GOOGLE_PLACES_BASE_URL = os.getenv("GOOGLE_PLACES_BASE_URL")


def search_place(dep_iata: str) -> dict:
    """
    """
    headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': api_key,
        'X-Goog-FieldMask': "places.displayName,places.location"
    }
    body = {
        "textQuery": f"{dep_iata} Airport" 
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
