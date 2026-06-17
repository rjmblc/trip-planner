import streamlit as st
from crew import travel_crew

st.set_page_config(
    page_title="AI Trip Planner",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ AI Trip Planner")
st.markdown(
    """
    Plan your trip using AI Agents.

    The application will:

    - ✈️ Search available flights
    - 🏨 Recommend nearby hotels
    - 📍 Suggest tourist attractions
    - 📝 Generate a complete travel itinerary
    """
)

col1, col2 = st.columns(2)

with col1:
    dep_iata = st.text_input(
        "Departure Airport (IATA)",
        placeholder="BLR"
    )

with col2:
    arr_iata = st.text_input(
        "Destination Airport (IATA)",
        placeholder="CDG"
    )

if st.button("Generate Travel Itinerary", use_container_width=True):

    if not dep_iata or not arr_iata:
        st.error("Please enter both airport codes.")
        st.stop()

    with st.spinner("Planning your trip..."):

        try:

            result = travel_crew.kickoff(
                inputs={
                    "dep_iata": dep_iata.upper(),
                    "arr_iata": arr_iata.upper()
                }
            )

            st.success("Trip planned successfully!")

            st.markdown("## 🧳 Travel Itinerary")

            st.markdown(result)

        except Exception as e:

            st.error(str(e))