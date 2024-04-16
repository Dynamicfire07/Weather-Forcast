import streamlit as st
import plotly.express as px

st.title("Weather forcast for the next days")
place = st.text_input("Place:",key="city")
days = st.slider("Forcast Days:", min_value=1,max_value=5,key="days",help="Select number of days of data you "
                                                                                "want to view")
listbox = st.selectbox(label="Select Data to View",
                       options=("Temperature","Sky"))

st.subheader(f"{listbox} for the {days} days in {place}")





d,t = get_data(place,days,option)
figure = px.line(x=d,y=t,labels={"x":"Dates",
                                                "y": "Temperatures/°C"})
st.plotly_chart(figure)


