# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt



tables = pd.read_html("https://www.feanalytics.com/Table.aspx?SavedResultsID=e33df1a2-7b9a-ee11-b204-002248818b97&xl=1&UserID=B2E540A8-D474-4C56-9088-1F155612F7FE&xlRefreshData=1")
#Saving the data into Dateframe
data = tables[0]
#Taking the transpose of table
data = data.T
#Spliting the dates from string format 
data[1][1][26:36]
#Looping into column and saving the dates in list 
dates = []
for i in range (1,71):
    date = data[1][i][26:36]
    dates.append(date)
#Droping the first and second columns
data = data.drop(columns=[0])
data = data.drop(columns=[1])
#Naming the columns 
data.columns = data.iloc[0]
data = data.iloc[1:].reset_index(drop=True)
#Now droping the Null values rows 
data.dropna(inplace = True)
#Adding the dates 
data['Dates'] = dates
#Converting the date into pandas datetime format
data['Dates'] = pd.to_datetime(data.Dates)
#Setting the Dates as index in our table
data.set_index('Dates', inplace= True)
#Changing the column data into float values
for i in range(len(data.columns)):
    data[data.columns[i]]=data[data.columns[i]].astype(float)



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