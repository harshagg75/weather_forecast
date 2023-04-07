import streamlit as st
import plotly.express as px
from backend import get_data


# add title , text input , slider and selctbox and subheader
st.title("WEATHER FORECAST FOR THE NEXT DAYS")
place = st.text_input("PLACE: ")
days = st.slider("Forecast Days: ", min_value=1, max_value=5, help="select the no. of days for the forecast weather")
option = st.selectbox("Select data to view: ",("Temperature","sky"))
st.subheader(f"{option} for the next {days} in {place}")


# get the temperature/sky data
if place:
    filter_data = get_data(place,days)


# create a temperature plot
    if option == "Temperature":
        temperature = [dict["main"]["temp"] for dict in filter_data]
        dates = [dict["dt_txt"] for dict in filter_data]
        figure = px.line(x=dates,y=temperature ,labels={"x":"dates", "y":"temperature(c)"})
        st.plotly_chart(figure)

    if option == "sky":
        images = {"Clear":"images/clear.png","Clouds":"images/cloud.png",
                  "Rain":"images/rain.png","Snow":"images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filter_data]
        image_path = [images[a] for a in sky_conditions]
        st.image(image_path,width=115)


