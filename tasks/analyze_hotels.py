from crewai import Task
from agent.suggest_hotels import analyst_agent

get_hotel_recommendations = Task(
    description=(
        "Search for hotels near the destination: {arr_iata}. "
        "Use the location search tool to identify the destination coordinates and "
        "retrieve nearby hotels. Analyze the available accommodations based on their "
        "location, ratings, amenities, and suitability for travelers. "
        "Provide a ranked list of recommended hotels along with key details and reasons for recommendation."
    ),

    expected_output=(
        "A clear, bullet-pointed summary of:\n"
        "- Hotel name\n"
        "- Location and distance from the destination\n"
        "- Rating and popularity\n"
        "- Available amenities\n"
        "- Why the hotel is recommended\n"
        "- Top 3-5 hotel recommendations ranked by suitability"
    ),

    agent=analyst_agent
)