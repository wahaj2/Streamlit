# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the app
st.title("My First Streamlit App")

# User input
st.write("## Enter a Number")
number = st.slider("Select a number", 1, 100, 50)

# Display the selected number
st.write(f"You selected: **{number}**")

# Create a line chart
st.write("## Line Chart")
data = pd.DataFrame({
    "x": range(number),
    "y": [i ** 2 for i in range(number)]
})
fig = px.line(data, x="x", y="y", title="y = x^2")
st.plotly_chart(fig)

# Add some text
st.write("## About This App")
st.write("This is a simple Streamlit app hosted on Streamlit Sharing. It demonstrates how to create interactive web apps using Python!")
