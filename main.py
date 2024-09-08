import streamlit as st

st.title('Weather Forecast for the Next Days')

place = st.text_input("Place:")

forecast_days = st.slider("Forecast Days", min_value=1, max_value=5,
                          help="Selecet the number of days you would like to forecast.")

option = st.selectbox("Select data to view", ["Temperature", "Sky"])

st.subheader(f"{option} for the next {forecast_days} days in {place}")


