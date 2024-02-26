#!/bin/bash

#SBATCH --job-name chemprop
#SBATCH --mail-user=Nikolenko.Sergei@icloud.com
#SBATCH --mail-type=FAIL, END
#SBATCH --ntasks=16
#SBATCH --gres=shard:5

export CUDA_VISIBLE_DEVICES=0

python train.py --log_freq 200 \
                --hidden_size 1028 \
                --batch_size 128 \
                --epochs 100 \
                --depth 9 \
                --save_smiles_splits \
                --dataset_type regression \
                --save_dir QM_137k \
                --data_path ../data/QM_137k_training.csv \
                --metric rmse \
                --show_individual_scores