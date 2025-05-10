import pandas as pd

# Load dataset
file_path = '/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/weatherAUS_after.csv'
data = pd.read_csv(file_path)

# Convert Date column in the main data to datetime for consistency
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Creating Dimension Tables

# Dim_Date
dim_date = data[['Date']].drop_duplicates().reset_index(drop=True)
dim_date['DateID'] = dim_date.index + 1
dim_date['Year'] = dim_date['Date'].dt.year
dim_date['Month'] = dim_date['Date'].dt.month
dim_date['Day'] = dim_date['Date'].dt.day
dim_date['DayOfWeek'] = dim_date['Date'].dt.day_name()

# Dim_Location
dim_location = data[['Location']].drop_duplicates().reset_index(drop=True)
dim_location['LocationID'] = dim_location.index + 1

# Dim_WeatherConditions
dim_weather_conditions = data[['WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday', 'RainTomorrow']].drop_duplicates().reset_index(drop=True)
dim_weather_conditions['ConditionID'] = dim_weather_conditions.index + 1

# Creating Fact Table

# Merge dimension tables with original data to create fact table
data = data.merge(dim_date, on='Date').merge(dim_location, on='Location').merge(dim_weather_conditions, 
                                                                                on=['WindGustDir', 'WindDir9am', 'WindDir3pm', 'RainToday', 'RainTomorrow'])

fact_weather = data[['DateID', 'LocationID', 'ConditionID', 'MinTemp', 'MaxTemp', 'Rainfall', 
                     'WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm', 
                     'Pressure9am', 'Pressure3pm', 'Temp9am', 'Temp3pm']]
fact_weather['WeatherFactID'] = fact_weather.index + 1

# Save tables to CSV files for output
dim_date.to_csv('/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/Dim_Date.csv', index=False)
dim_location.to_csv('/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/Dim_Location.csv', index=False)
dim_weather_conditions.to_csv('/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/Dim_WeatherConditions.csv', index=False)
fact_weather.to_csv('/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/Fact_Weather.csv', index=False)

{
    "dim_date": "/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/Dim_Date.csv",
    "dim_location": "/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/Dim_Location.csv",
    "dim_weather_conditions": "/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/Dim_WeatherConditions.csv",
    "fact_weather": "/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/Fact_Weather.csv"
}

