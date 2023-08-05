import streamlit as st
import plotly.express as px
from backend import get_data

st.title("WEATHER FORECASTER")
city = st.text_input("Enter Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days through this slider")
options = st.selectbox(options=("Temperature", "Sky"), label="options")
st.subheader(f"{options} for the next {days} days in {city}")

if city:
    try:
        filtered_data = get_data(city, days)

        if options == "Temperature":
            temp = [fd["main"]["temp"] for fd in filtered_data]
            temp = [(((i - 273.115) * 9/5 + 32) - 32) * 5/9 for i in temp]
            dates = [fd["dt_txt"] for fd in filtered_data]
            figure = px.line(x=dates, y=temp, labels={"x": "date", "y": "temperature (c)"})
            st.plotly_chart(figure)

        if options == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [fd["weather"][0]["main"] for fd in filtered_data]
            image_path = [images[condition] for condition in sky_conditions]
            st.image(image_path, width=110)
    except KeyError:
        st.info("OOPS! THIS PLACE DOES NOT EXIST. PLEASE ENTER A VALID CITY NAME")


