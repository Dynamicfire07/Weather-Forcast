import streamlit as st


st.title("Weather forcast for the next days")
place = st.text_input("Place:",key="city")
no_of_days = st.slider("Forcast Days:", min_value=1,max_value=5,key="days",help="Select number of days of data you "
                                                                                "want to view")
listbox = st.selectbox(label="Select Data to View",
                       options=("Temperature","Sky"))

st.subheader(f"{listbox} for the {no_of_days} days in {place}")

