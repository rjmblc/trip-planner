from crewai import Task
from agent.analyse_agent import travel_planner_agent


get_travel_analysis = Task(
    description=(
        "Plan a trip from {dep_iata} to {arr_iata}. "
        "Use the travel details tool to retrieve available flights, airport information, "
        "nearby hotels, and tourist attractions for the destination. "
        "Analyze all the retrieved information and identify the best travel options based on "
        "flight schedules, accommodation quality, convenience, and nearby attractions. "
        "Provide a structured travel analysis that will help another agent generate the final itinerary."
    ),

    expected_output=(
        "A structured travel analysis report containing:\n"
        "- Departure and destination airports\n"
        "- Available flight options (airline, flight number, departure & arrival times)\n"
        "- Airport details (name and location)\n"
        "- Recommended nearby hotels\n"
        "- Popular tourist attractions near the destination\n"
        "- Key observations and recommendations that will be used to create the final travel itinerary"
    ),

    agent=travel_planner_agent
)