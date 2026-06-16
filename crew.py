from crewai import Crew

from tasks.analyze_hotels import get_hotel_recommendations

from agent.suggest_hotels import analyst_agent


stock_crew = Crew(
    agents=[analyst_agent],
    tasks=[get_hotel_recommendations],
    verbose=True
)