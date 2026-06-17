from crewai import Crew

from tasks.analyse_task import get_travel_analysis
from tasks.trip_planner_task import generate_travel_itinerary
from agent.analyse_agent import travel_planner_agent
from agent.trip_planner_agent import travel_itinerary_agent

stock_crew = Crew(
    agents=[travel_planner_agent, travel_itinerary_agent],
    tasks=[get_travel_analysis, generate_travel_itinerary],
    verbose=True
)