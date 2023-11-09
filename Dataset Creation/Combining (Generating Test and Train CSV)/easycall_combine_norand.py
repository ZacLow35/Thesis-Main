import os
import pandas as pd
import random  # Added the 'random' module
import sys

input_folder = sys.argv[1]
output_file = sys.argv[2]  # Added a new variable for the 'test' file

# Usage: python easycall_combine_norand.py <input_folder_path> <output_file>

def combine_csv_files(input_folder, output_file):
    # Create an empty list to store data from each CSV file
    all_data = []

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_folder, filename)
            # Read each CSV file into a DataFrame and append it to the list
            df = pd.read_csv(file_path)
            all_data.append(df)

    # Concatenate all DataFrames in the list into a single DataFrame
    combined_data = pd.concat(all_data, ignore_index=True)

    # Save the 'train' and 'test' DataFrames to separate CSV files
    
    combined_data.to_csv(output_file, index=False)

if __name__ == "__main__":
    combine_csv_files(input_folder, output_file)
    print(output_file + ' has been created.')
