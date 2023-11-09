** Note: The shell scripts (.sh files) are to be taken with a grain of salt. They show how to run each python file, 
but may be outdated and was not used to run code. For what I actually ran on the terminal, look at scrapnote.bat.

scrapnote.bat:
This is not a real batch file, it contains code that I ran manually on the terminal.
Use this file to see how I ran my code and take advantage of the multiple GPUs available on katana.

--------- Main Model -------------
audioClass_Combination.py: Main training model, it also tests every epoch and keeps the best checkpoint.
audioClass_inference.py: Takes checkpoint from trained model and can be tested on other datasets.

--------- Dataset Creation ---------
easycall_combine_norand.py: Despite the name, it isn't only for the EasyCall dataset. This code just takes .csv files in 2 folders - train and test - and combines them into a train.csv and test.csv file.
easycall_sev_binary_label.py: Binary labelling of EasyCall dataset based on EasyCall file structure.
torgo_binary_label.py: Binary labelling of TORGO dataset based on TORGO file structure.

\Thesis Main\Dataset Creation\Examples: Look at the .csv file to see how the models read the .csv file.

--------- Speaking Rate -----------
voiceActivation.py: Uses pyannote for voice activation to detect the length of speech.
speakRateAug.py: Uses sox to change speaking rate without changing pitch. Stores the .wav file in a separate directory, and clears the directory every new run to save space.
augData_label.py: Labels the .wav files created by speakRateAug.py in a csv file.