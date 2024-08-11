#!/bin/bash

set -euo pipefail

CPU=2 #selecting cpus
MEM=300000 #selecting memory 
GROUP="team298" #selecting group to submit with 
#GMEM=40000 #selecting gpu conditions: memory, gpu cores, whether to shared gpu
QUE="week" #selecting queue to submit to
# if GMEM < 30GB you can use "gpu-normal", "gpu-huge" or "gpu-basement"
# if you need GMEM >30GB use QUE="gpu-cellgeni-a100"
NAME=subset_data


# ##################### DONT CHANGE OPTIONS BELOW THIS LINE ###########################

mkdir -p logs
bsub -o logs/$NAME.txt -e logs/$NAME.err -n $CPU -Rspan[hosts=1] -M $MEM -R"select[mem>${MEM}] rusage[mem=${MEM}]" -G $GROUP -q $QUE ./run_execute_notebook.sh