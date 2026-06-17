from dotenv import load_dotenv
from crew import stock_crew


load_dotenv()

def run(dep_iata: str,arr_iata: str):
    result = stock_crew.kickoff(inputs={"dep_iata": dep_iata,"arr_iata": arr_iata})
    print(result)


if __name__ == "__main__":
    run("BLR","AMS")