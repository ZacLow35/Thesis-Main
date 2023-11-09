# 1. visit hf.co/pyannote/segmentation and accept user conditions
# 2. visit hf.co/settings/tokens to create an access token
# 3. instantiate pretrained voice activity detection pipeline

# Usage: python voiceActivation.py folder_path csv_file

import sys
import os
import csv
from pyannote.audio import Pipeline

folder_path = sys.argv[1] 
csv_file = sys.argv[2]

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['File Name', 'Speaker Length'])

pipeline = Pipeline.from_pretrained("pyannote/voice-activity-detection",
                                    use_auth_token="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")

wav_files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]

for wav_file in wav_files:
    audio_path = os.path.join(folder_path, wav_file)
    output = pipeline(audio_path)

    speechlength = 0
    for speech in output.get_timeline().support():
        speechlength += speech.end - speech.start

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([wav_file, speechlength])

print('Processing complete. Results are saved in', csv_file)
