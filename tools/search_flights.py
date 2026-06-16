import requests
import os
from dotenv import load_dotenv

# load .env to environment
load_dotenv()

access_key = os.getenv("access_key")
SEARCH_FLIGHTS_BASE_URL = os.getenv("SEARCH_FLIGHTS_BASE_URL")

def search_flights(arr_iata: str, dep_iata: str) -> dict:
    """ This function returns the flights information based on the departure and arrival city iata codes"""
    params = {
        'access_key' : access_key,
        'limit' : 100,
        'offset' : 0,
        'callback' : 'MY_CALLBACK',
        'arr_iata' : arr_iata,
        'dep_iata' : dep_iata
    }
    response = requests.get(SEARCH_FLIGHTS_BASE_URL, params = params)
    result = response.json()
    flights = []
    for flight in result["data"]:
        flights.append({
            "flight_date": flight["flight_date"],
            "airline_name": flight["airline"]["name"],
            "flight_number": flight["flight"]["number"],
            "departure_time": flight["departure"]["scheduled"],
            "arrival_time": flight["arrival"]["scheduled"]

        })
    return flights

res = search_flights('MAA','BLR')
for items in res:
    print(res)
