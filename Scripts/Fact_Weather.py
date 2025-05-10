import pyodbc
import pandas as pd

# Database connection setup (replace placeholders with actual values)
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=WeatherDB;UID=SA;PWD=12345abcd#')
cursor = conn.cursor()

# Load CSV file into a DataFrame, excluding the WeatherFact_ID column
file_path = '/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/Weather_Fact.csv'  # Replace with the actual path
weather_fact_data = pd.read_csv(
    file_path, 
    dtype={
        'Location_ID': int,
        'Date_ID': int,
        'WeatherCondition_ID': int,
        'MinTemp': float,
        'MaxTemp': float,
        'Rainfall': float,
        'WindGustSpeed': float,
        'WindSpeed9am': float,
        'WindSpeed3pm': float,
        'Humidity9am': float,
        'Humidity3pm': float,
        'Pressure9am': float,
        'Pressure3pm': float,
        'Temp9am': float,
        'Temp3pm': float
    }
)

# Replace any NaN values with None (SQL NULL)
weather_fact_data = weather_fact_data.where(pd.notnull(weather_fact_data), None)

# Insert data into Weather_Fact table
for index, row in weather_fact_data.iterrows():
    cursor.execute("""
    INSERT INTO Weather_Fact (
        Location_ID, Date_ID, WeatherCondition_ID, MinTemp, MaxTemp, Rainfall, 
        WindGustSpeed, WindSpeed9am, WindSpeed3pm, Humidity9am, Humidity3pm, 
        Pressure9am, Pressure3pm, Temp9am, Temp3pm
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, row.Location_ID, row.Date_ID, row.WeatherCondition_ID, row.MinTemp, row.MaxTemp, row.Rainfall, 
       row.WindGustSpeed, row.WindSpeed9am, row.WindSpeed3pm, row.Humidity9am, row.Humidity3pm, 
       row.Pressure9am, row.Pressure3pm, row.Temp9am, row.Temp3pm)
conn.commit()

# Close the connection
cursor.close()
conn.close()

print("Data loaded successfully into Weather_Fact table.")
