from crew import travel_crew

def run_trip_planner(dep_iata: str, arr_iata: str):
    return travel_crew.kickoff(
        inputs={
            "dep_iata": dep_iata,
            "arr_iata": arr_iata
        }
    )