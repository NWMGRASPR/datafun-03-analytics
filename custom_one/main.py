"""custom_one.main.py - This is the script for this custom_one project.
Author: Ralph Massaquoi
2026-05

This simple project contains an excel table with 10 cities alone with their populations.
ChatGBT helped with this project. These cities are the most populated cities in the United States.
"""
import pandas as pd

# Data for 10 cities
data = {
    "City": [
        "New York",
        "Los Angeles",
        "Chicago",
        "Houston",
        "Phoenix",
        "Philadelphia",
        "San Antonio",
        "San Diego",
        "Dallas",
        "San Jose"
    ],
    "Population": [
        8336817,
        3898747,
        2746388,
        2304580,
        1608139,
        1576251,
        1434625,
        1386932,
        1304379,
        1013240
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("cities_population.xlsx", index=False)

print("Excel file 'cities_population.xlsx' created successfully.")
