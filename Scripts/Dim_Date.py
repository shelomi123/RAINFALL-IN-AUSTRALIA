
import pyodbc
import pandas as import pdb; pdb.set_trace()
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=WeatherDB;UID=SA;PWD=12345abcd#')
cursor = conn.cursor()

file_path = '/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/Time_Dim.csv'  
time_dim_data = pd.read_csv(file_path, usecols=['Date', 'Year', 'Month', 'Day', 'Quarter'])


for index, row in time_dim_data.iterrows():
    cursor.execute("""
    INSERT INTO Time_Dim (Date, Year, Month, Day, Quarter)
    VALUES (?, ?, ?, ?, ?)
    """, row.Date, row.Year, row.Month, row.Day, row.Quarter)
conn.commit()

# Close the connection
cursor.close()
conn.close()

print("Data loaded successfully into Time_Dim table.")
