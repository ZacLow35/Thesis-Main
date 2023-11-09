from datasets import load_dataset, Audio
import pandas as pd
import soundfile as sf
import sys
import resampy
from transformers import AutoFeatureExtractor, AutoModelForAudioClassification, TrainingArguments, Trainer, EvalPrediction
import evaluate
import numpy as np

# Define the paths and file names
model_checkpoint = sys.argv[1]        # Replace with the actual path to your saved model
test_csv = sys.argv[2]              # Replace with the path to your new test CSV file

# Load the pre-trained model
model = AutoModelForAudioClassification.from_pretrained(model_checkpoint)

# Load the feature extractor
feature_extractor = AutoFeatureExtractor.from_pretrained("facebook/wav2vec2-large-xlsr-53")

# Load evaluation metrics
cfm_metric = evaluate.load("BucketHeadP65/confusion_matrix")
accuracy = evaluate.load("accuracy")

# Load and preprocess the new test dataset
new_test_data = load_dataset('csv', data_files={'test': test_csv}, cache_dir="/srv/scratch/z5271785/augCache")
new_test_data = new_test_data.cast_column("File Path", Audio(sampling_rate=16000))

def resample_audio(audio_array, source_sr, target_sr):
    return resampy.resample(audio_array, source_sr, target_sr)

def preprocess_function(examples):
    audio_arrays = [x["array"] for x in examples["File Path"]]
    
    # Upsample to 16 kHz if the source sampling rate is 8 kHz
    sampling_rate = feature_extractor.sampling_rate
    if sampling_rate == 8000:
        audio_arrays = [resample_audio(audio, 8000, 16000) for audio in audio_arrays]
    
    inputs = feature_extractor(
        audio_arrays, sampling_rate=feature_extractor.sampling_rate, max_length=2*16000, truncation=True
    )
    return inputs

new_test_data = new_test_data.map(preprocess_function, remove_columns="File Path", batched=True)
new_test_data = new_test_data.rename_column("Label", "label")

# Evaluate the model on the new test dataset
from transformers import EvalPrediction

def compute_metrics(eval_pred: EvalPrediction):
    predictions = np.argmax(eval_pred.predictions, axis=1)
    cfm_results = cfm_metric.compute(references=eval_pred.label_ids, predictions=predictions, labels=[0, 1])
    
    # Misclassification:
    misclassified_indices = []
    for i in range(len(eval_pred.label_ids)):
        if eval_pred.label_ids[i] != predictions[i]:
            misclassified_indices.append(i)

    print()
    print(cfm_results)  # Print Confusion Matrix
    print()
    print("Misclassified samples indices:", misclassified_indices)
    print()

    return accuracy.compute(predictions=predictions, references=eval_pred.label_ids)  # Compute Accuracy

# Use the Trainer class for evaluation
from transformers import Trainer

trainer = Trainer(
    model=model,
    tokenizer=feature_extractor,
    compute_metrics=compute_metrics,
)

# Evaluate on the new test dataset
results = trainer.evaluate(eval_dataset=new_test_data["test"])
print("Evaluation Results on New Test Dataset:", results)
