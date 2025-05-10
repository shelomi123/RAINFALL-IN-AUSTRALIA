import pandas as pd
import numpy as np
from datetime import datetime

def clean_weather_data(input_file, output_file):
    """
    Main function to perform all data cleaning steps on the weather dataset
    and save the cleaned data to a single output file.

    Parameters:
    - input_file: str, path to the original CSV file.
    - output_file: str, path to save the fully cleaned CSV file.
    """
    # Load the initial dataset
    data = pd.read_csv(input_file)

    # 1. Drop columns with a high percentage of missing values (threshold 35%)
    data = check_null_percent_and_drop_blank_columns(data)

    # 2. Clean direction columns to keep only N, E, W, S and replace blanks with "NULL"
    data = count_and_clean_direction_data(data)

    # 3. Round off outliers in Humidity columns and replace blanks with 0
    data = humidity_round_off_outliers_and_replace_blanks(data)

    # 4. Convert Date column to "YYYY-MM-DD" format
    data = convert_date_format(data)

    # 5. Check and clean RainToday and RainTomorrow columns (only YES, NO, or blanks allowed)
    data = check_and_replace_rain_columns(data)

    # 6. Replace blanks with 0 in specific columns
    columns_to_replace = ['MinTemp', 'MaxTemp', 'Rainfall', 'WindGustSpeed', 
                          'WindSpeed9am', 'WindSpeed3pm', 'Pressure9am', 
                          'Pressure3pm', 'Temp9am', 'Temp3pm']
    data = replace_blanks_with_zero(data, columns_to_replace)

    # Save the fully cleaned data to a CSV file
    data.to_csv(output_file, index=False)
    print(f"\nAll data cleaning steps complete. Cleaned data saved to '{output_file}'.")

def check_null_percent_and_drop_blank_columns(data, threshold=35):
    blank_cells_count = data.isna().sum()
    total_rows = len(data)
    blank_columns = blank_cells_count[blank_cells_count > 0]
    blank_percentages = (blank_columns / total_rows) * 100
    columns_to_drop = blank_percentages[blank_percentages > threshold].index.tolist()
    data = data.drop(columns=columns_to_drop)
    print(f"Dropped columns with more than {threshold}% blanks: {columns_to_drop}")
    return data

def count_and_clean_direction_data(data):
    columns_to_check = ['WindGustDir', 'WindDir9am', 'WindDir3pm']
    allowed_chars = {'N', 'E', 'W', 'S'}
    rows_to_drop = []

    def is_valid_direction(value):
        return set(str(value)).issubset(allowed_chars)

    for index, row in data.iterrows():
        if any(not is_valid_direction(row[col]) for col in columns_to_check):
            rows_to_drop.append(index)

    data = data.drop(index=rows_to_drop)
    data[columns_to_check] = data[columns_to_check].applymap(lambda x: "NULL" if pd.isna(x) or str(x).strip() == '' else x)
    print(f"Dropped rows with invalid direction data: {len(rows_to_drop)} rows dropped.")
    return data

def humidity_round_off_outliers_and_replace_blanks(data):
    
    columns_to_check = ['Humidity9am', 'Humidity3pm']
    def process_value(value):
        if pd.isna(value) or str(value).strip() == '': return 0
        elif value < 0: return 0
        elif value > 100: return 100
        else: return value
    for col in columns_to_check:
        data[col] = data[col].apply(process_value)
    print("Rounded outliers and replaced blanks with 0 in Humidity columns.")
    return data

def convert_date_format(data, date_column='Date'):
    def parse_date(value):
        try:
            return datetime.strptime(value, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            for fmt in ("%d/%m/%Y", "%d-%m-%Y", "%m/%d/%Y", "%Y/%m/%d"):
                try:
                    return datetime.strptime(value, fmt).strftime("%Y-%m-%d")
                except ValueError:
                    continue
            return "NULL"
    data[date_column] = data[date_column].astype(str).apply(parse_date)
    print("Converted Date column to 'YYYY-MM-DD' format.")
    return data

def check_and_replace_rain_columns(data):
    columns_to_check = ['RainToday', 'RainTomorrow']
    allowed_values = {'YES', 'NO'}
    for col in columns_to_check:
        data[col] = data[col].apply(lambda x: "NULL" if pd.isna(x) or str(x).strip().upper() not in allowed_values else x)
    print("Replaced invalid values in RainToday and RainTomorrow columns with 'NULL'.")
    return data

def replace_blanks_with_zero(data, columns_to_replace):
    data[columns_to_replace] = data[columns_to_replace].fillna(0)
    print(f"Replaced blanks with 0 in specified columns: {columns_to_replace}")
    return data

# Usage example
input_file = '/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/weatherAUS_before.csv' 
output_file = '/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/weatherAUS_after.csv' 

clean_weather_data(input_file,output_file)
