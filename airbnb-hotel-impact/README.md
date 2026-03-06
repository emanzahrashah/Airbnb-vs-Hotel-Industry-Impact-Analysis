Airbnb Growth vs Hotel Industry Impact
Project Overview

This project analyzes the relationship between the growth of Airbnb listings and hotel industry wages across major U.S. cities from 2014 to 2023. The goal of this analysis is to explore whether the expansion of short-term rentals has negatively impacted the traditional hotel industry.

Using publicly available datasets, this project combines Airbnb listing data with U.S. Bureau of Labor Statistics hotel wage data to examine trends across multiple metropolitan areas.

The project includes data cleaning, exploratory analysis, visualizations, and an interactive dashboard to explore the relationship between Airbnb growth and hotel industry wages.

Cities Analyzed

The analysis focuses on five major U.S. cities:

Chicago

Seattle

New York

Los Angeles

San Francisco

Dataset Sources

Airbnb Data

Inside Airbnb dataset

Includes listing information such as price, location, and reviews

Hotel Industry Data

U.S. Bureau of Labor Statistics (BLS)

Quarterly Census of Employment and Wages

Industry: NAICS 72111 – Hotels (except casino hotels)

Methods Used

The project follows a complete end-to-end data science workflow:

Data collection from multiple sources

Data cleaning and preprocessing

Feature engineering and aggregation

Exploratory data analysis (EDA)

Visualization of trends across cities

Development of an interactive dashboard using Plotly Dash

Python libraries used:

Pandas

NumPy

Matplotlib

Plotly

Dash

Interactive Dashboard

An interactive dashboard was developed using Plotly Dash to explore Airbnb growth and hotel industry wages across cities.

Users can:

Select different cities

View trends in Airbnb listings over time

Compare Airbnb growth with hotel industry wages

Dashboard preview:




Key Insights

Several important insights emerged from the analysis:

Airbnb listings increased significantly in most cities between 2014 and 2023, with rapid growth after 2021.

The COVID-19 pandemic in 2020 caused a major decline in hotel industry wages across all cities.

Despite the growth of Airbnb listings, hotel wages recovered after the pandemic, suggesting the hotel industry remained resilient.

The results indicate that Airbnb and hotels appear to coexist, serving different segments of the travel market rather than directly replacing one another.

Project Structure
airbnb-hotel-impact
│
├── dashboard
│   ├── dashboard.py
│   └── final_airbnb_hotel_dataset.csv
│
├── data
│
├── notebooks
│   └── 01_airbnb_hotel_impact_analysis.ipynb
│
├── images
│   └── dashboard_preview.png
│
└── README.md
How to Run the Dashboard

Navigate to the dashboard folder and run:

python dashboard.py

Then open the browser and visit:

http://127.0.0.1:8050
Future Improvements

Possible future improvements include:

Incorporating tourism demand data

Analyzing hotel occupancy rates

Studying the impact of Airbnb regulations in different cities

Expanding the analysis to additional metropolitan areas

Author

Eman Zahra