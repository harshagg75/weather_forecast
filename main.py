import streamlit as st

st.title("WEATHER FORECAST FOR THE NEXT DAYS")
place = st.text_input("PLACE: ")
days = st.slider("Forecast Days: ", min_value=1, max_value=5, help="select the no. of days for the forecast weather")
option = st.selectbox("Select data to view: ",("Temperature","sky"))
st.subheader(f"{option} for the next {days} in {place}")

