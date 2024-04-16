import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forcast for the next days")
place = st.text_input("Place:", key="city")
days = st.slider("Forcast Days:", min_value=1, max_value=5, key="days", help="Select number of days of data you "
                                                                             "want to view")
option = st.selectbox(label="Select Data to View",
                      options=("Temperature", "Sky"))

st.subheader(f"{option} for the {days} days in {place}")

try:
    filtered_data = get_data(place=place, forcast_days=days)

    if option == "Temperature":
        try:
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Dates",
                                                          "y": "Temperatures/°C"})
            st.plotly_chart(figure)
        except KeyError:
            st.write("Unfortunately, That Place Doesnt Exist on Earth!")

    if option == "Sky":
        images = {
            "Clear": "images/clear.png",
            "Clouds": "images/cloud.png",
            "Rain": "images/rain.png",
            "Snow": "images/snow.png",
        }
        sky_conds = [dict["weather"][0]["main"] for dict in filtered_data]
        image_path = [images[condition] for condition in sky_conds]
        dates = [dict["dt_txt"] for dict in filtered_data]
        st.image(image_path, width=150, caption=dates)
except KeyError:
    st.warning("This Place Doesnt Exist!")