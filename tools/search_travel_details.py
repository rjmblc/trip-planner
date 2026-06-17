import requests
from dotenv import load_dotenv
import os
from crewai.tools import tool

# load .env variables to environment
load_dotenv()

access_key = os.getenv("access_key")
SEARCH_FLIGHTS_BASE_URL = os.getenv("SEARCH_FLIGHTS_BASE_URL")
GOOGLE_PLACES_BASE_URL = os.getenv("GOOGLE_PLACES_BASE_URL")
GOOGLE_HOTELS_BASE_URL = os.getenv("GOOGLE_HOTELS_BASE_URL")
GOOGLE_TOURIST_PLACES_BASE_URL = os.getenv("GOOGLE_TOURIST_PLACES_BASE_URL")
GOOGLE_PLACES_API_KEY = os.getenv("X-Goog-Api-Key")

@tool("Search Travel Details")
def search_travel_details(arr_iata: str, dep_iata: str) -> dict:
    """
    Retrieves comprehensive travel information for a given departure and destination airport.

    The tool searches for available flights between the specified airports, identifies the
    destination airport's location, finds nearby hotels, and recommends popular tourist
    attractions around the destination. The collected information can be used by an AI
    travel planner to generate personalized travel recommendations and itineraries.

    Parameters:
        arr_iata (str): IATA code of the arrival airport (e.g., JFK, CDG, MAA).

        dep_iata (str): IATA code of the departure airport (e.g., BLR, LAX, DEL).

    Returns:
        dict: A dictionary containing the following travel information:

            - flights (list):
                Available flight options including airline name, flight number,
                departure time, arrival time, and flight date.

            - places (list):
                Destination airport details including airport name,
                latitude, and longitude.

            - hotels (list):
                Nearby hotel recommendations around the destination airport.

            - tourist_places (list):
                Popular tourist attractions and their addresses near
                the destination.
    
    
    """
    flights_params = {
        'access_key' : access_key,
        'limit' : 100,
        'offset' : 0,
        'callback' : 'MY_CALLBACK',
        'arr_iata' : arr_iata,
        'dep_iata' : dep_iata
    }
    flights_response = requests.get(SEARCH_FLIGHTS_BASE_URL, params = flights_params)
    result = flights_response.json()
    flights = []
    for flight in result["data"]:
        flights.append({
            "flight_date": flight["flight_date"],
            "airline_name": flight["airline"]["name"],
            "flight_number": flight["flight"]["number"],
            "departure_time": flight["departure"]["scheduled"],
            "arrival_time": flight["arrival"]["scheduled"]

        })

    places_headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': GOOGLE_PLACES_API_KEY,
        'X-Goog-FieldMask': "places.displayName,places.location"
    }
    places_body = {
        "textQuery": f"{arr_iata} Airport" 
    }
    places_response = requests.post(GOOGLE_PLACES_BASE_URL,headers=places_headers,json=places_body)
    output = places_response.json()
    place_list = []
    for details in output["places"]:
        place_list.append({
            "latitude" : details["location"]["latitude"],
            "longitude" : details["location"]["longitude"],
            "airport_name" : details["displayName"]["text"]
        })

    
    hotels_body = {
        "includedTypes": ["hotel", "lodging"],
        "maxResultCount": 10,
        "locationRestriction": {
        "circle": {
            "center": {
                "latitude": place_list[0]["latitude"],
                "longitude": place_list[0]["longitude"]
                },
                "radius": 50000.0
                  }
                               }
            }
    
    hotels_response = requests.post(GOOGLE_HOTELS_BASE_URL,headers=places_headers,json=hotels_body)
    output = hotels_response.json()
    hotels = []
    for hotel in output["places"]:
        hotels.append({
            "Hotel Name" : hotel["displayName"]["text"]
        })

    tourist_places_headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': GOOGLE_PLACES_API_KEY,
        'X-Goog-FieldMask': "places.displayName,places.formattedAddress,places.priceLevel"
    }


    places_to_visit_body ={
        "textQuery" : f"Best places to visit around {place_list[0]['airport_name']}"
        }

    tourist_places_response = requests.post(GOOGLE_TOURIST_PLACES_BASE_URL,headers=tourist_places_headers,json=places_to_visit_body)
    output = tourist_places_response.json()
    tourist_places = []
    for places in output["places"]:
        tourist_places.append({
            "placeAddress" : places["formattedAddress"],
            "placename" : places["displayName"]["text"]
        })

    return {
    "flights": flights,
    "hotels": hotels,
    "places": place_list,
    "tourist_places": tourist_places
    }