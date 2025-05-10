import pyodbc
import pandas as pd

# Database connection setup (replace placeholders with actual values)
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=WeatherDB;UID=SA;PWD=12345abcd#')
cursor = conn.cursor()

# Load CSV file into a DataFrame, explicitly setting column types to string (text)
file_path = '/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/WeatherCondition_Dim2_copy2.csv'  # Replace with the actual path
weather_condition_data = pd.read_csv(
    file_path, 
    dtype={
        'RainToday': str,
        'RainTomorrow': str,
        'WindGustDir': str,
        'WindDir9am': str,
        'WindDir3pm': str
    }
)

weather_condition_data = weather_condition_data.astype(str).replace('nan', None)

# Insert data into WeatherCondition_Dim table
for index, row in weather_condition_data.iterrows():
    cursor.execute("""
    INSERT INTO WeatherConditions_Dim (RainToday, RainTomorrow, WindGustDir, WindDir9am, WindDir3pm)
    VALUES (?, ?, ?, ?, ?)
    """, row.RainToday, row.RainTomorrow, row.WindGustDir, row.WindDir9am, row.WindDir3pm)
conn.commit()

# Close the connection
cursor.close()
conn.close()

print("Data loaded successfully into WeatherCondition_Dim table.")
