import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
@st.cache_data
def load_data():
    data = pd.read_csv('data.csv')
    return data

data = load_data()

# Convert the 'Dates' column to datetime
data['Dates'] = pd.to_datetime(data['Dates'])

# Set the 'Dates' column as the index
data.set_index('Dates', inplace=True)

# Get the list of sectors
sectors = data.columns.tolist()

# Streamlit app
st.title('Sector Performance Dashboard')

# Dropdown to select a sector
selected_sector = st.selectbox('Select a Sector', sectors)

# Plot the selected sector's data
st.write(f"### {selected_sector} Performance Over Time")
fig, ax = plt.subplots()
ax.plot(data.index, data[selected_sector], label=selected_sector)
ax.set_xlabel('Date')
ax.set_ylabel('Performance')
ax.legend()
st.pyplot(fig)