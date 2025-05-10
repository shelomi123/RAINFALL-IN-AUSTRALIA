import pandas as pd

# Load both CSV files
weather_fact = pd.read_csv('/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/Weather_Fact.csv')  # Replace with actual path
weather_condition_dim = pd.read_csv('/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/WeatherCondition_Dim2_copy2.csv')  # Replace with actual path

# Find WeatherCondition_IDs in Weather_Fact that are missing in WeatherCondition_Dim
missing_ids = set(weather_fact['WeatherCondition_ID']) - set(weather_condition_dim['WeatherCondition_ID'])

if missing_ids:
    print("Missing WeatherCondition_IDs in WeatherCondition_Dim:", missing_ids)
else:
    print("All WeatherCondition_IDs in Weather_Fact.csv are present in WeatherCondition_Dim.csv.")
