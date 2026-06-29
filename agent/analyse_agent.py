from crewai import Agent, LLM

from tools.search_travel_details import search_travel_details
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the LLM
llm = LLM(
    model=MODEL_NAME,
    api_key=GEMINI_API_KEY,
    temperature=0.0
)

travel_planner_agent = Agent(
    role="AI Travel Planner and Itinerary Specialist",

    goal=(
        "Analyze available flight options, airport information, nearby hotels, and tourist attractions "
        "to create a personalized, well-organized travel itinerary. Recommend the best flight, "
        "accommodation, and sightseeing plan that optimizes convenience, travel time, comfort, "
        "and overall travel experience."
    ),

    backstory=(
        "You are a professional travel consultant with years of experience planning domestic and "
        "international vacations, business trips, and family holidays. You excel at analyzing "
        "flight schedules, airport locations, hotel options, and nearby tourist attractions to "
        "design practical and enjoyable travel itineraries. Your recommendations balance traveler "
        "convenience, accommodation quality, sightseeing opportunities, and efficient use of time. "
        "You provide structured, easy-to-follow itineraries with clear recommendations and reasons "
        "for each choice."
    ),

    llm=llm,
    tools=[search_travel_details],
    verbose=True
)