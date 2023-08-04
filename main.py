import streamlit as st

st.title("WEATHER FORECASTER")
place = st.text_input("Enter Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of days through this slider")
options = st.selectbox(options=["temperature", "sky"], label="options")
st.subheader(f"{options} for the next {days} days in {place}")
