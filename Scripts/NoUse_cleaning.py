import csv
import re
import pandas as pd
import numpy as np

#Removing special characters in Dim_WeatherConditions
def clean_csv_special_char(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            # Clean each cell in the row
            cleaned_row = [re.sub(r'[^a-zA-Z0-9\s]', '', cell) for cell in row]
            writer.writerow(cleaned_row)




# Replace 'input.txt' and 'output.txt' with the paths to your actual files
input_file_path = '/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/WeatherCondition_Dim2_copy.csv'
output_file_path = '/Users/shelomi/Documents/UNITEC/Data Warehouse and Big data/Assignment2/dataset/files/WeatherCondition_Dim2_copy2.csv'
clean_csv_special_char(input_file_path, output_file_path)

