import os
import csv
import sys

input_directory = "/srv/scratch/z5271785/augData"
output_directory = "/srv/scratch/z5271785/augData"
label = sys.argv[1]

def create_wav_csv(input_dir, output_dir, label):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Initialize a list to store the file paths
    file_paths = []

    # Traverse the input directory to find .wav files
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".wav"):
                file_paths.append(os.path.join(root, file))

    # Create a CSV file to store the file paths and labels
    csv_file_path = os.path.join(output_dir, f"augData.csv")

    with open(csv_file_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["File Path", "Label"])

        for file_path in file_paths:
            writer.writerow([file_path, label])

    print(f"CSV file '{csv_file_path}' created with {len(file_paths)} entries.")

# Example usage


create_wav_csv(input_directory, output_directory, label)
