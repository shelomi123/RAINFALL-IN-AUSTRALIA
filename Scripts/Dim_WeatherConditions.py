import pyodbc
import pandas as pd


conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=WeatherDB;UID=SA;PWD=12345abcd#')
cursor = conn.cursor()


file_path = '/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/WeatherCondition_Dim.csv' 
weather_condition_data = pd.read_csv(file_path, usecols=['RainToday', 'RainTomorrow', 'WindGustDir', 'WindDir9am', 'WindDir3pm'])

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
