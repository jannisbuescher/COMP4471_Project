#!usr/bin/env bash
# select gpu devices
#export CUDA_VISIBLE_DEVICES=6,7
export OMP_NUM_THREADS=1

python -m CHR.main --workers 0 --batch-size 320 2>&1 | tee -a log
 
