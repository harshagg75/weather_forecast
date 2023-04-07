import streamlit as st
import plotly.express as px

st.title("WEATHER FORECAST FOR THE NEXT DAYS")
place = st.text_input("PLACE: ")
days = st.slider("Forecast Days: ", min_value=1, max_value=5, help="select the no. of days for the forecast weather")
option = st.selectbox("Select data to view: ",("Temperature","sky"))
st.subheader(f"{option} for the next {days} in {place}")


def get_date(days):
    dates = ["2022-25-10","2022-26-10","2022-27-10"]
    temperature = [10,11,15]
    temperature = [days * i for i in temperature]
    return dates, temperature

d,t = get_date(days)

figure = px.line(x = d,y = t ,labels={"x":"dates", "y":"temperature(c)"})
st.plotly_chart(figure)