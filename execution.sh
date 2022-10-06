#!/bin/bash

# # # vertical_dataset 만들기
# # # python make_vertical_data.py

# # # horizontal_dataset 만들기
# # # python make_horizontal_data.py

# # # train lmdb dataset 생성
# # # python create_lmdb_dataset.py --inputPath ./data/not_lmdb --gtFile data/train_horizontal.csv --outputPath data/train_horizontal_lmdb_dataset
# # # python create_lmdb_dataset.py --inputPath ./data/not_lmdb --gtFile data/train_vertical.csv --outputPath data/train_vertical_rotate_lmdb_dataset

# # # val lmdb dataset 생성
# # # python create_lmdb_dataset.py --inputPath ./data/not_lmdb --gtFile data/val_vertical.csv --outputPath data/val_vertical_rotate_lmdb_dataset
# # # python create_lmdb_dataset.py --inputPath ./data/not_lmdb --gtFile data/val_horizontal.csv --outputPath data/val_horizontal_lmdb_dataset

# # # test lmdb dataset 생성
# # # python create_lmdb_dataset.py --inputPath ./data/not_lmdb --gtFile data/test_horizontal.csv --outputPath data/test_horizontal_lmdb_dataset
# # # python create_lmdb_dataset.py --inputPath ./data/not_lmdb --gtFile data/test_vertical.csv --outputPath data/test_vertical_rotate_lmdb_dataset

# train.py 실행
python train.py --manualSeed 9991 --adam --lr 5e-4 --imgH 240 --imgW 750 --train_data /home/lab/sangminnim/train_horizontal_lmdb_dataset_2 --valid_data /home/lab/sangminnim/val_horizontal_lmdb_dataset --saved_model /home/lab/sangminnim/pretrained/horizontal/maybe_best_h.pth --FT --batch_size 32 --num_iter 100000 --valInterval 1000 --select_data basic --batch_ratio 1.0 --batch_max_length 30 --data_filtering_off --Transformation TPS --FeatureExtraction VGG --SequenceModeling BiLSTM --Prediction Attn;
# python train.py --manualSeed 9992 --adam --lr 5e-4 --imgH 240 --imgW 750 --train_data /home/lab/sangminnim/train_vertical_rotate_lmdb_dataset_2 --valid_data /home/lab/sangminnim/val_vertical_rotate_lmdb_dataset --saved_model /home/lab/sangminnim/pretrained/vertical/maybe_best_v.pth --FT --batch_size 32 --num_iter 50000 --valInterval 1000 --select_data basic --batch_ratio 1.0 --batch_max_length 30 --data_filtering_off --Transformation TPS --FeatureExtraction VGG --SequenceModeling BiLSTM --Prediction Attn;

# test.py 실행 (test.py에 validation func)
# python test.py --saved_model saved_models/TPS-VGG-BiLSTM-Attn-Seed1/best_accuracy.pth --imgH 32 --imgW 100 --eval_data data/test_horizontal_lmdb_dataset --batch_size 16 --batch_max_length 30 --data_filtering_off --Transformation TPS --FeatureExtraction VGG --SequenceModeling BiLSTM --Prediction Attn;
# python test.py --saved_model saved_models/TPS-VGG-BiLSTM-Attn-Seed2/best_accuracy.pth --imgH 32 --imgW 100 --eval_data data/test_vertical_rotate_lmdb_dataset --batch_size 16 --batch_max_length 30 --data_filtering_off --Transformation TPS --FeatureExtraction VGG --SequenceModeling BiLSTM --Prediction Attn;
