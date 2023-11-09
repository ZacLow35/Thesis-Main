import csv
import sys

# Usage: python /srv/scratch/z5271785/EasyCall/f01/f01.txt <flag> ; flag = 0 is control, flag = 1 is severity

input_file = sys.argv[1]  # Give path to .txt file from EasyCall library
flag = sys.argv[2]        # Severity Flag 
x, speaker_name = input_file.rsplit('/',1) # Split last /
output_file = '/srv/scratch/z5271785/main/datasets/EasyCall_binsev/sev_data/' + speaker_name[:-4]+ '_sev.csv' # Get rid of .txt, and add '.csv'
word_file = 'wordfile.txt'
sym_text = "â€™"                        # ' in L'alto Read in as this by python
act_text = "’"                          # The actual symbol corresponding to sym_text

# Open the input and output files
with open(input_file, 'r') as file:
    lines = file.readlines()

with open(word_file, 'r') as file:
    words = [word.strip() for word in file.readlines()]  # Strip newlines from words

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['File Path', 'Label'])  # Write the header

    # Process each line and write to the CSV file
    for line in lines:
        line = line.strip()
        file_path = line
        file_path = file_path.replace(sym_text,act_text)        # Replace the error symbol text, to be able to access path
        writer.writerow(['/srv/scratch/z5271785/EasyCall/' + file_path, flag]) # Binary dysarthric label

if (flag == '0'):
    print(f"CSV file '{output_file}' has been generated. Control")
elif (flag <= '5'):
    print(f"CSV file '{output_file}' has been generated. Dysarthric level " + flag)
else:
    print(f"Unrecognized flag")
