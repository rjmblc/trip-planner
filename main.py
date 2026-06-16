from dotenv import load_dotenv
from crew import stock_crew


load_dotenv()

def run(arr_iata: str, dep_iata: str):
    result = stock_crew.kickoff(inputs={"arr_iata": arr_iata, "dep_iata": dep_iata})
    print(result)


if __name__ == "__main__":
    run("BLR", "MAA")