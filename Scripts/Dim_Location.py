import pyodbc
import pandas as pd


conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=WeatherDB;UID=SA;PWD=12345abcd#')
cursor = conn.cursor()

file_path = '/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/Location_Dim.csv' 
location_dim_data = pd.read_csv(file_path, usecols=['Location'])


for index, row in location_dim_data.iterrows():
    cursor.execute("""
    INSERT INTO Location_Dim (Location)
    VALUES (?)
    """, row.Location)
conn.commit()

# Close the connection
cursor.close()
conn.close()

print("Data loaded successfully into Location_Dim table.")
