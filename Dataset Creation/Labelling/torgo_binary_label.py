import os
import csv
import argparse

def list_wav_files(folder_path):
    wav_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".wav"):
                wav_files.append(os.path.join(root, file))
    return wav_files

def save_to_csv(file_paths, flag, output_filename):
    with open(output_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["File Path", "Label"])
        for file_path in file_paths:
            csv_writer.writerow([file_path, flag])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a CSV file containing .wav file paths and flags.")
    parser.add_argument("folder_path", help="Path to the folder containing .wav files")
    parser.add_argument("flag", help="Flag to associate with the file paths")
    parser.add_argument("output_filename", help="Name of the output CSV file")
    args = parser.parse_args()

    folder_path = args.folder_path
    flag = args.flag
    output_filename = args.output_filename

    wav_files = list_wav_files(folder_path)
    if wav_files:
        save_to_csv(wav_files, flag, output_filename)
        print(f"CSV file '{output_filename}' created successfully.")
    else:
        print("No .wav files found in the specified folder.")
