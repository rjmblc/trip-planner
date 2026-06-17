# ✈️ AI Trip Planner using CrewAI

An AI-powered multi-agent travel planning application that generates personalized travel itineraries by combining flight information, nearby hotel recommendations, and tourist attractions.

The application leverages **CrewAI** to orchestrate AI agents that gather travel information from multiple sources and generate an optimized travel itinerary using **Groq Llama 3.3 70B**.


## 🚀 Features

* ✈️ Search available flights between departure and destination airports
* 📍 Retrieve airport details using Google Places API
* 🏨 Recommend nearby hotels
* 🌍 Discover popular tourist attractions around the destination
* 🤖 Multi-agent workflow using CrewAI
* 📝 Generate an AI-powered personalized travel itinerary
* 💻 Streamlit-based user interface


## 🏗️ Architecture

```text
                User
                  │
                  ▼
          Streamlit Frontend
                  │
                  ▼
          CrewAI Multi-Agent System
                  │
      ┌───────────┴────────────┐
      │                        │
      ▼                        ▼
Travel Analysis Agent     Trip Planner Agent
      │                        │
      └───────────┬────────────┘
                  │
                  ▼
          Travel Search Tools
                  │
     ┌────────────┼────────────┐
     │            │            │
     ▼            ▼            ▼
 Flight API   Google Places   Google Nearby Search
                  │
                  ▼
           AI Generated Itinerary
```
## 🧠 AI Agents

### Travel Analysis Agent

Responsible for:

* Searching available flights
* Retrieving airport details
* Finding nearby hotels
* Discovering tourist attractions
* Producing a structured travel analysis

### Trip Planner Agent

Responsible for:

* Analyzing travel information
* Selecting the best flight
* Recommending suitable accommodation
* Planning sightseeing
* Generating a complete travel itinerary

## 🛠️ Tools

The application consists of reusable AI tools:

* Flight Search Tool
* Airport Search Tool
* Hotel Search Tool
* Tourist Attractions Search Tool

## 📦 Tech Stack

* Python 3.11
* CrewAI
* Groq (Llama 3.3 70B)
* Streamlit
* Google Places API
* Google Nearby Search API
* AviationStack API
* Requests
* Python Dotenv


## 📂 Project Structure

```text
trip-planner/
│
├── agent/
│   ├── analyse_agent.py
│   └── trip_planner_agent.py
│
├── tasks/
│   ├── analyse_task.py
│   └── trip_planner_task.py
│
├── tools/
│   ├── search_flights.py
│   ├── search_place.py
│   ├── search_hotels.py
│   └── search_tourist_places.py
│
├── crew.py
├── main.py
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/rjmblc/trip-planner.git
```

Navigate to the project

```bash
cd trip-planner
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root.

```text
GROQ_API_KEY=your_groq_api_key

SEARCH_FLIGHTS_BASE_URL=https://api.aviationstack.com/v1/flights
GOOGLE_PLACES_BASE_URL=https://places.googleapis.com/v1/places:searchText
GOOGLE_HOTELS_BASE_URL=https://places.googleapis.com/v1/places:searchNearby
GOOGLE_TOURIST_PLACES_BASE_URL=https://places.googleapis.com/v1/places:searchText

access_key=your_aviationstack_key
X-Goog-Api-Key=your_google_places_key
```

## ▶️ Run the Application

Run the Streamlit frontend

```bash
streamlit run app.py
```

## 📸 Screenshots

### Home Page

![alt text](image-1.png)

### Generated Travel Itinerary

![alt text](image.png)

## 🎯 Learning Outcomes

This project demonstrates:

* Multi-Agent AI Systems
* Tool Calling
* Prompt Engineering
* LLM Orchestration
* API Integration
* AI-powered Travel Planning
* Python Application Development
* Streamlit Frontend Development

## 👨‍💻 Author

Rajmohan B

GitHub: https://github.com/rjmblc

LinkedIn: https://www.linkedin.com/in/rajmohan-balachandran-29199a45/

