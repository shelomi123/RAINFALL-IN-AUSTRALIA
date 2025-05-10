import pandas as pd

# Load the CSV files
weather_fact = pd.read_csv('/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/Weather_Fact.csv')  # Replace with actual path
weather_condition_dim = pd.read_csv('/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/WeatherABC.csv')  # Replace with actual path

# Print column names to check if WeatherCondition_ID exists
print("Columns in Weather_Fact.csv:", weather_fact.columns)
print("Columns in WeatherCondition_Dim.csv:", weather_condition_dim.columns)

# Only proceed if both have the required column
if 'WeatherCondition_ID' in weather_fact.columns and 'WeatherCondition_ID' in weather_condition_dim.columns:
    # Find WeatherCondition_IDs in Weather_Fact that are missing in WeatherCondition_Dim
    missing_ids = set(weather_fact['WeatherCondition_ID']) - set(weather_condition_dim['WeatherCondition_ID'])
    
    if missing_ids:
        print("Missing WeatherCondition_IDs in WeatherCondition_Dim:", missing_ids)
    
else:
    print("Error: One of the files is missing the 'WeatherCondition_ID' column.")
