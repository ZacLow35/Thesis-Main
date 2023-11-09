---- EasyCall Leave One Out -----
python ./datasets/EasyCall_binsev/easycall_combine_norand.py /srv/scratch/z5271785/main/datasets/EasyCall_binsev/train /srv/scratch/z5271785/main/datasets/EasyCall_binsev/train.csv
python ./datasets/EasyCall_binsev/easycall_combine_norand.py /srv/scratch/z5271785/main/datasets/EasyCall_binsev/test /srv/scratch/z5271785/main/datasets/EasyCall_binsev/test.csv

CUDA_VISIBLE_DEVICES=1 python audioClass_Combination.py EC1 ZLOW/EC1_bin /srv/scratch/z5271785/main/datasets/EasyCall_binsev/train.csv /srv/scratch/z5271785/main/datasets/EasyCall_binsev/test.csv

CUDA_VISIBLE_DEVICES=2 python audioClass_Combination.py EC2 ZLOW/EC2_bin /srv/scratch/z5271785/main/datasets/EasyCall_binsev/train.csv /srv/scratch/z5271785/main/datasets/EasyCall_binsev/test.csv

CUDA_VISIBLE_DEVICES=3 python audioClass_Combination.py EC3 ZLOW/EC3_bin /srv/scratch/z5271785/main/datasets/EasyCall_binsev/train.csv /srv/scratch/z5271785/main/datasets/EasyCall_binsev/test.csv

---- TORGO Leave One Out -----
python ./datasets/EasyCall_binsev/easycall_combine_norand.py /srv/scratch/z5271785/main/datasets/TORGO_binsev/train /srv/scratch/z5271785/main/datasets/TORGO_binsev/train.csv
python ./datasets/EasyCall_binsev/easycall_combine_norand.py /srv/scratch/z5271785/main/datasets/TORGO_binsev/test /srv/scratch/z5271785/main/datasets/TORGO_binsev/test.csv

CUDA_VISIBLE_DEVICES=0 python audioClass_Combination.py TG0 ZLOW/TG0_bin /srv/scratch/z5271785/main/datasets/TORGO_binsev/train.csv /srv/scratch/z5271785/main/datasets/TORGO_binsev/test.csv

CUDA_VISIBLE_DEVICES=1 python audioClass_Combination.py TG1 ZLOW/TG1_bin /srv/scratch/z5271785/main/datasets/TORGO_binsev/train.csv /srv/scratch/z5271785/main/datasets/TORGO_binsev/test.csv

CUDA_VISIBLE_DEVICES=2 python audioClass_Combination.py TG2 ZLOW/TG2_bin /srv/scratch/z5271785/main/datasets/TORGO_binsev/train.csv /srv/scratch/z5271785/main/datasets/TORGO_binsev/test.csv

CUDA_VISIBLE_DEVICES=3 python audioClass_Combination.py TG3 ZLOW/TG3_bin /srv/scratch/z5271785/main/datasets/TORGO_binsev/train.csv /srv/scratch/z5271785/main/datasets/TORGO_binsev/test.csv

---- Combination -----
python ./datasets/EasyCall_binsev/easycall_combine_norand.py /srv/scratch/z5271785/main/datasets/Combination_binsev/train /srv/scratch/z5271785/main/datasets/Combination_binsev/train.csv
python ./datasets/EasyCall_binsev/easycall_combine_norand.py /srv/scratch/z5271785/main/datasets/Combination_binsev/test /srv/scratch/z5271785/main/datasets/Combination_binsev/test.csv

CUDA_VISIBLE_DEVICES=0 python audioClass_Combination.py CM0 ZLOW/CM0_bin /srv/scratch/z5271785/main/datasets/Combination_binsev/train.csv /srv/scratch/z5271785/main/datasets/Combination_binsev/test.csv

CUDA_VISIBLE_DEVICES=2 python audioClass_Combination.py CM2 ZLOW/CM2_bin /srv/scratch/z5271785/main/datasets/Combination_binsev/train.csv /srv/scratch/z5271785/main/datasets/Combination_binsev/test.csv

-- 2 --
python ./datasets/EasyCall_binsev/easycall_combine_norand.py /srv/scratch/z5271785/main/datasets/Combination_binsev/train /srv/scratch/z5271785/main/datasets/Combination_binsev/train2.csv
python ./datasets/EasyCall_binsev/easycall_combine_norand.py /srv/scratch/z5271785/main/datasets/Combination_binsev/test /srv/scratch/z5271785/main/datasets/Combination_binsev/test2.csv

CUDA_VISIBLE_DEVICES=1 python audioClass_Combination.py CM1 ZLOW/CM1_bin /srv/scratch/z5271785/main/datasets/Combination_binsev/train2.csv /srv/scratch/z5271785/main/datasets/Combination_binsev/test2.csv

CUDA_VISIBLE_DEVICES=3 python audioClass_Combination.py CM3 ZLOW/CM3_bin /srv/scratch/z5271785/main/datasets/Combination_binsev/train2.csv /srv/scratch/z5271785/main/datasets/Combination_binsev/test2.csv

----------- speakRateAug -------------
python speakRateAug.py /srv/scratch/z5271785/EasyCall/fc05 0.9
python augData_label.py 0 

python ./datasets/EasyCall_binsev/easycall_combine_norand.py /srv/scratch/z5271785/main/datasets/Combination_binsev/train /srv/scratch/z5271785/main/datasets/Combination_binsev/train2.csv
python ./datasets/EasyCall_binsev/easycall_combine_norand.py /srv/scratch/z5271785/main/datasets/Combination_binsev/test /srv/scratch/z5271785/main/datasets/Combination_binsev/test2.csv

CUDA_VISIBLE_DEVICES=1 python audioClass_Combination.py CM1 ZLOW/CM1_bin /srv/scratch/z5271785/main/datasets/Combination_binsev/train2.csv /srv/scratch/z5271785/main/datasets/Combination_binsev/test2.csv

-- HEALTHY -- 
python speakRateAug.py /srv/scratch/z5271785/TORGO/M03 1
python augData_label.py 0 
python audioClass_inference.py /srv/scratch/z5271785/main/ZLOW/CM0_bin/checkpoint-237 /srv/scratch/z5271785/augData/augData.csv

python speakRateAug.py /srv/scratch/z5271785/EasyCall/m154 0.9
python augData_label.py 0 
python audioClass_inference.py /srv/scratch/z5271785/main/ZLOW/CM2_bin/checkpoint-232 /srv/scratch/z5271785/augData/augData.csv

python speakRateAug.py /srv/scratch/z5271785/EasyCall/m154 0.7
python augData_label.py 0 
python audioClass_inference.py /srv/scratch/z5271785/main/ZLOW/CM2_bin/checkpoint-232 /srv/scratch/z5271785/augData/augData.csv

python speakRateAug.py /srv/scratch/z5271785/EasyCall/m154 0.5
python augData_label.py 0 
python audioClass_inference.py /srv/scratch/z5271785/main/ZLOW/CM2_bin/checkpoint-232 /srv/scratch/z5271785/augData/augData.csv

python speakRateAug.py /srv/scratch/z5271785/EasyCall/m154 0.3
python augData_label.py 0 
python audioClass_inference.py /srv/scratch/z5271785/main/ZLOW/CM2_bin/checkpoint-232 /srv/scratch/z5271785/augData/augData.csv

python speakRateAug.py /srv/scratch/z5271785/EasyCall/m154 0.1
python augData_label.py 0 
python audioClass_inference.py /srv/scratch/z5271785/main/ZLOW/CM2_bin/checkpoint-232 /srv/scratch/z5271785/augData/augData.csv

python speakRateAug.py /srv/scratch/z5271785/EasyCall/m154 1.5
python augData_label.py 0 
python audioClass_inference.py /srv/scratch/z5271785/main/ZLOW/CM2_bin/checkpoint-232 /srv/scratch/z5271785/augData/augData.csv



-- DYSARTHRIC --

python speakRateAug.py /srv/scratch/z5271785/TORGO/M05 1
python augData_label.py 1 
python audioClass_inference.py /srv/scratch/z5271785/main/ZLOW/CM3_bin/checkpoint-479 /srv/scratch/z5271785/augData/augData.csv

python speakRateAug.py /srv/scratch/z5271785/EasyCall/f01 3
python augData_label.py 1 
python audioClass_inference.py /srv/scratch/z5271785/main/ZLOW/CM0_bin/checkpoint-238 /srv/scratch/z5271785/augData/augData.csv

python speakRateAug.py /srv/scratch/z5271785/EasyCall/f01 2.1
python augData_label.py 1 
python audioClass_inference.py /srv/scratch/z5271785/main/ZLOW/CM0_bin/checkpoint-238 /srv/scratch/z5271785/augData/augData.csv

python speakRateAug.py /srv/scratch/z5271785/EasyCall/f01 1.9
python augData_label.py 1 
python audioClass_inference.py /srv/scratch/z5271785/main/ZLOW/CM0_bin/checkpoint-238 /srv/scratch/z5271785/augData/augData.csv

python speakRateAug.py /srv/scratch/z5271785/EasyCall/f01 1.7
python augData_label.py 1 
python audioClass_inference.py /srv/scratch/z5271785/main/ZLOW/CM0_bin/checkpoint-238 /srv/scratch/z5271785/augData/augData.csv

python speakRateAug.py /srv/scratch/z5271785/EasyCall/f01 1.5
python augData_label.py 1 
python audioClass_inference.py /srv/scratch/z5271785/main/ZLOW/CM0_bin/checkpoint-238 /srv/scratch/z5271785/augData/augData.csv

python speakRateAug.py /srv/scratch/z5271785/EasyCall/f01 1.3
python augData_label.py 1 
python audioClass_inference.py /srv/scratch/z5271785/main/ZLOW/CM0_bin/checkpoint-238 /srv/scratch/z5271785/augData/augData.csv

python speakRateAug.py /srv/scratch/z5271785/EasyCall/f01 1.1
python augData_label.py 1 
python audioClass_inference.py /srv/scratch/z5271785/main/ZLOW/CM0_bin/checkpoint-238 /srv/scratch/z5271785/augData/augData.csv

python speakRateAug.py /srv/scratch/z5271785/EasyCall/f01 0.5
python augData_label.py 1
python audioClass_inference.py /srv/scratch/z5271785/main/ZLOW/CM0_bin/checkpoint-238 /srv/scratch/z5271785/augData/augData.csv
