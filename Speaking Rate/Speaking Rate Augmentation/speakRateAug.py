import os
import subprocess
import sys

directory = sys.argv[1]
factor = sys.argv[2]

import os
import subprocess

def speech_augmentation(directory, factor):
    output_directory = '/srv/scratch/z5271785/augData'
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Create the output directory or clear its contents
    if os.path.exists(output_directory):
        for file in os.listdir(output_directory):
            file_path = os.path.join(output_directory, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                for sub_file in os.listdir(file_path):
                    sub_file_path = os.path.join(file_path, sub_file)
                    if os.path.isfile(sub_file_path):
                        os.unlink(sub_file_path)
        print(f"Cleared the contents of '{output_directory}'.")
    else:
        os.makedirs(output_directory)

    index = 1
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.wav'):
                input_path = os.path.join(root, file)

                # Generate the output filename with the index
                output_filename = f"{os.path.splitext(file)[0]}_{index}.wav"
                output_path = os.path.join(output_directory, output_filename)

                # Run the sox command with the specified tempo factor
                cmd = ['sox', input_path, output_path, 'tempo', str(factor)]
                subprocess.run(cmd)

                index += 1  # Increment the index for the next file


                #print(f"Processed: {input_path} -> {output_path}")

if __name__ == "__main__":
    speech_augmentation(directory, factor)
    print("speakRateAug completed")
