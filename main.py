import streamlit as st
import plotly.express as px

def get_data(forecast_days, place):
    dates = ["2024-08-09", "2024-08-08", "2024-08-07"]
    temperatures = [26, 22, 25]
    temperatures = [forecast_days * i for i in temperatures]
    return dates, temperatures

# User interface
st.title('Weather Forecast for the Next Days')
place = st.text_input("Place:")
forecast_days = st.slider("Forecast Days", min_value=1, max_value=5,
                          help="Selecet the number of days you would like to forecast.")
option = st.selectbox("Select data to view", ["Temperature", "Sky"])
st.subheader(f"{option} for the next {forecast_days} days in {place}")


dates, temperatures = get_data(forecast_days, place)

figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(figure)
