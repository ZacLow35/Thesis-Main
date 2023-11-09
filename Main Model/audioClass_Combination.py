from datasets import load_dataset, Audio
import pandas as pd
import soundfile as sf
import sys
import resampy

folder = sys.argv[1]        # Folder name ; not actually used in code
repo_name = sys.argv[2]     # Huggingface Repo
csv_train1 = sys.argv[3]    # Train CSV (Big csv file)
csv_test = sys.argv[4]      # Test CSV (Smaller csv file)

################ Load Data ################

data = load_dataset('csv', 
                     data_files= {'train': csv_train1, 'test': csv_test},
                     cache_dir="/srv/scratch/z5271785/")

# Map label to integer
labels = data["train"].unique("Label")
label2id, id2label = dict(), dict() # Initialize 2 empty dictionaries.
for i, label in enumerate(labels):
    label2id[label] = str(i)
    id2label[str(i)] = label

################ Preprocess ################

from transformers import AutoFeatureExtractor

feature_extractor = AutoFeatureExtractor.from_pretrained("facebook/wav2vec2-large-xlsr-53")

data = data.cast_column("File Path", Audio(sampling_rate=16000))

# Function to upsample audio to 16 kHz
def resample_audio(audio_array, source_sr, target_sr):
    return resampy.resample(audio_array, source_sr, target_sr)

def preprocess_function(examples):
    audio_arrays = [x["array"] for x in examples["File Path"]]
    
    # Upsample to 16 kHz if the source sampling rate is 8 kHz
    sampling_rate = feature_extractor.sampling_rate
    if sampling_rate == 8000:
        audio_arrays = [resample_audio(audio, 8000, 16000) for audio in audio_arrays]
        print("in \n")
    
    inputs = feature_extractor(
        audio_arrays, sampling_rate=feature_extractor.sampling_rate, max_length=2*16000, truncation=True
    )
    return inputs

encoded_data = data.map(preprocess_function, remove_columns="File Path", batched=True)
encoded_data = encoded_data.rename_column("Label", "label")

################ Evaluate ################

import evaluate

cfm_metric = evaluate.load("BucketHeadP65/confusion_matrix")
accuracy = evaluate.load("accuracy")

import numpy as np

def compute_metrics(eval_pred):
    predictions = np.argmax(eval_pred.predictions, axis=1)
    cfm_results = cfm_metric.compute(references=eval_pred.label_ids, predictions=predictions, labels=[0,1])
    
    # Misclassification :
    misclassified_indices = []
    for i in range(len(eval_pred.label_ids)):
        if eval_pred.label_ids[i] != predictions[i]:
            misclassified_indices.append(i)

    print()
    print(cfm_results) # Print Confusion Matrix
    print() 
    print("Misclassified samples indices:", misclassified_indices)
    print()

    return accuracy.compute(predictions=predictions, references=eval_pred.label_ids) # Compute Accuracy

################ Train ################
from transformers import AutoModelForAudioClassification, TrainingArguments, Trainer

num_labels = len(id2label)
model = AutoModelForAudioClassification.from_pretrained(
    "facebook/wav2vec2-large-xlsr-53", num_labels=num_labels, label2id=label2id, id2label=id2label
)

training_args = TrainingArguments(
    output_dir=repo_name,
    evaluation_strategy="epoch", # Performance evaluated every epoch
    save_strategy="epoch",       # Snapshots of model's parameters at every epoch
    learning_rate=3e-5,
    per_device_train_batch_size=32, # Steps per epoch = Total number of training samples / Batch size
    gradient_accumulation_steps=4,
    per_device_eval_batch_size=32,
    num_train_epochs=10,
    warmup_ratio=0.1,
    logging_steps=10,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    push_to_hub=False,
    save_total_limit=1,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=encoded_data["train"],
    eval_dataset=encoded_data["test"],
    tokenizer=feature_extractor,
    compute_metrics=compute_metrics,
)

trainer.train()

#trainer.save_model(repo_name) # Maybe get rid of this