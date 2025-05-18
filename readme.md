

```markdown
# 🚇 Delhi Metro Data Analysis App

## 📌 Overview

This **Streamlit** application provides interactive visualizations and insights into **Delhi Metro Station Data**, covering:

- **Metro Line Distribution:** Pie chart of station proportions by line.
- **Station Locations:** Interactive map displaying metro stations across Delhi.
- **Number of Stations per Line:** Bar chart for comparison.
- **Distance Analysis:** Histogram of station distances from the first stop.
- **Yearly Openings:** Line graph showing metro expansion trends.
- **Metro Station Layouts:** Stacked bar chart comparing underground/elevated stations.

## 🔧 Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/shaik-1036/delhi-metro-data-analysis.git
   ```
   ```bash
   cd delhi-metro-data-analysis/
   ```


2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## 📂 Data Source

The dataset **Delhi Metro.csv** contains key station details, including:

- **Metro Line**
- **Station Name**
- **Latitude & Longitude**
- **Distance from First Station**
- **Opening Year**
- **Layout (Elevated, Underground, etc.)**

## 📊 Features & Visualizations

1. **Metro Line Distribution:**  
   - Pie chart displaying station proportions by **metro line**.
   - Helps understand which lines are most prominent.

2. **Interactive Map of Metro Stations:**  
   - Uses **Folium** to visualize station locations with GPS coordinates.
   - Click on markers to view **station names**.

3. **Number of Stations per Metro Line:**  
   - **Bar chart** to compare total metro stations across lines.
   - Helpful for analyzing metro development across Delhi.

4. **Distance Distribution Analysis:**  
   - Histogram displaying station distances from the **first stop**.
   - Shows how metro lines are structured across the city.

5. **Yearly Openings Trend:**  
   - Line chart showing how **metro expansion** has progressed yearly.

6. **Metro Station Layouts:**  
   - **Stacked bar chart** comparing underground, elevated, and surface stations.

## 🎨 Technologies Used

- **Python**
- **Streamlit** (for interactive UI)
- **Pandas** (data handling)
- **NumPy**
- **Matplotlib & Seaborn** (visualizations)
- **Plotly & Folium** (interactive charts/maps)

## 💡 Future Improvements

- Adding **real-time metro tracking**.
- Expanding analysis to **passenger traffic**.
- Enhancing **route optimization insights**.

## 📝 Author

Developed by **[Shaik Allabakash]**  
