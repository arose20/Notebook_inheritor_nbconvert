#!/bin/bash

set -euo pipefail

CPU=1 #selecting cpus
MEM=2000 #selecting memory 
GROUP="team298" #selecting group to submit with 
QUE="normal" #selecting queue to submit to
NAME=example_1


# ##################### DONT CHANGE OPTIONS BELOW THIS LINE ###########################

mkdir -p logs
bsub -o logs/$NAME.txt -e logs/$NAME.err -n $CPU -Rspan[hosts=1] -M $MEM -R"select[mem>${MEM}] rusage[mem=${MEM}]" -G $GROUP -q $QUE ./run_execute_notebook.sh