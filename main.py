import streamlit as st
import plotly.express as px
from backend import get_data


# User interface
st.title('Weather Forecast for the Next Days')
place = st.text_input("Place:")
forecast_days = st.slider("Forecast Days", min_value=1, max_value=5,
                          help="Selecet the number of days you would like to forecast.")
kind = st.selectbox("Select data to view", ["Graph", "Sky"])

if (place != ""):
    try:
        dates, weather_data, icon_urls= get_data(place, forecast_days, kind)
        st.subheader(f"{kind} for the next {forecast_days} days in {place}")

        if kind == "Graph":
            figure = px.line(x=dates, y=weather_data, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        elif kind == "Sky":
            cols = st.columns(6)
            i = 0
            for date, temp, url in zip(dates, weather_data, icon_urls):
                with cols[i % 6]:
                    image_caption = f"{date} {temp} C"
                    st.image(url, caption=image_caption)
                    i += 1
    except Exception as e:
        print(e)
        st.error("Make sure that you entered name of the city correctly.")
