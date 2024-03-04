#!/bin/bash

#SBATCH --job-name=hyper
#SBATCH --ntasks=8
#SBATCH --gres=shard:2

export CUDA_VISIBLE_DEVICES=0


source /opt/anaconda3/bin/activate chemprop


python hyper.py


conda deactivate