from crewai import Task
from agent.trip_planner_agent import travel_itinerary_agent


generate_travel_itinerary = Task(
    description=(
        "Using the travel analysis report prepared by the Travel Analysis Agent, "
        "evaluate the available flight options, airport details, nearby hotels, "
        "and tourist attractions to create a personalized travel itinerary. "
        "Select the most suitable flight and accommodation, organize the sightseeing "
        "schedule, and provide practical travel recommendations that maximize "
        "convenience, comfort, and overall travel experience."
    ),

    expected_output=(
        "A comprehensive travel itinerary containing:\n"
        "- Recommended flight (airline, flight number, departure and arrival times)\n"
        "- Recommended hotel with reasons for selection\n"
        "- Suggested tourist attractions organized into a logical itinerary\n"
        "- Recommended order of visiting places\n"
        "- Practical travel tips and local transportation suggestions\n"
        "- A final summary explaining why these recommendations provide the best travel experience"
    ),

    agent=travel_itinerary_agent
)