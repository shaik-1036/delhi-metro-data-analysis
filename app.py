import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import folium
from streamlit_folium import folium_static

# App Title
st.title("🚇 Delhi Metro Data Analysis App")
st.write("""
### Project Overview
This app analyzes **Delhi Metro station data**, providing insights into the metro line distributions, distances, openings, and layouts.
You'll find **interactive charts and maps** to visualize trends in the dataset.
""")

# -----------------------------------------------------
# 📌 Step 1: Import & Load the Data
# -----------------------------------------------------

st.write("## 📂 Data Loading")
st.write("""
The dataset is automatically loaded from a predefined file in the `data/Delhi metro.csv` folder. 
It contains information on Delhi Metro **stations, their locations, distances, and openings**.
""")

DATA_PATH = "./data/Delhi metro.csv"  # Your data file location
df = pd.read_csv(DATA_PATH)

# Display Data Preview
st.write("### Preview of Data")
st.write(df.head())

# -----------------------------------------------------
# 📌 Step 2: Data Cleaning & Missing Values
# -----------------------------------------------------

st.write("## 🛠 Data Cleaning")
st.write("""
Before analysis, it's **essential to clean the data** to remove missing values and ensure proper formatting.
This section removes incomplete entries and checks for inconsistencies.
""")

# Checking for Missing Values
st.write("### Missing Values")
st.write(df.isnull().sum())

# Data Cleaning
df_cleaned = df.dropna()
st.write("### Cleaned Data")
st.write(df_cleaned.head())

# -----------------------------------------------------
# 📌 Step 3: Generating Insigts from Delhi Metro
# -----------------------------------------------------

st.write("## 📊 Metro Line Distribution")
st.write("""
This pie chart shows **the proportion of metro stations** under different metro lines.
It helps understand which metro lines have the highest number of stations.
""")

line_colors = {
    'Red line': 'red', 'Yellow line': 'yellow', 'Blue line': 'blue', 'Blue line branch': 'navy',
    'Green line branch': 'forestgreen', 'Green line': 'green', 'Rapid Metro': 'silver', 
    'Voilet line': 'purple', 'Magenta line': 'magenta', 'Pink line': 'pink',
    'Aqua line': 'skyblue', 'Gray line': 'gray', 'Orange line': 'orange'
}
line_counts = df_cleaned['Metro Line'].value_counts()
fig = px.pie(names=line_counts.index, values=line_counts, title="Metro Line Distribution")
st.plotly_chart(fig)



st.write("## 🗺 Metro Station Locations")
st.write("""
This interactive map shows the locations of metro stations in **Delhi** using GPS coordinates.
Click on markers to view station names.
""")

delhi_map = folium.Map(location=[28.6139, 77.2090], zoom_start=12)
for _, row in df_cleaned.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=row['Station Names']).add_to(delhi_map)
folium_static(delhi_map)



st.write("## 📊 Number of Stations per Metro Line")
st.write("""
This bar chart displays **the total number of metro stations** for each metro line.
It helps compare different lines and their station distributions.
""")

fig = px.bar(df_cleaned, x="Metro Line", title="Number of Stations per Metro Line")
st.plotly_chart(fig)



st.write("## 📏 Distance from First Station")
st.write("""
This histogram shows the **distribution of distances** from the first station of each metro line.
It helps analyze station positioning across different metro routes.
""")

fig = px.histogram(df_cleaned, x="Dist. From First Station(km)", nbins=20, title="Distribution of Distances")
st.plotly_chart(fig)



st.write("## 📅 Yearly Openings of Metro Stations")
st.write("""
This line chart tracks **the number of new metro stations opened each year**.
It helps identify trends in metro expansion over time.
""")

yearly_openings = df.groupby('Opened(Year)').size().reset_index(name="count")
fig = px.line(yearly_openings, x="Opened(Year)", y="count", markers=True, title="Yearly Openings")
st.plotly_chart(fig)



st.write("## 🏗 Metro Station Layouts")
st.write("""
This stacked bar chart visualizes **different metro station layouts** (e.g., underground, elevated, etc.) across metro lines.
It helps compare how stations are designed for each metro line.
""")

layout_by_line = pd.crosstab(df_cleaned['Layout'], df_cleaned['Metro Line'])
colors = [line_colors[line] for line in layout_by_line.columns if line in line_colors]
layout_by_line.plot(kind='bar', stacked=True, figsize=(10, 6), color=colors)
plt.xlabel('Layout')
plt.ylabel('Count')
plt.title('Layout Distribution by Metro Line')
plt.legend(title='Metro Line', loc='upper left', bbox_to_anchor=(1, 1))
st.pyplot(plt)