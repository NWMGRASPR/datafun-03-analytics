def greet():
    print("Hello from custom_one!")


if __name__ == "__main__":
    greet()
####
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
