#!/bin/bash

# Prompt the user for input
#read -p "Enter the kernel name: " kernel_name
#read -p "Enter the template file: " template_file
#read -p "Enter the output file name: " output_file
#read -p "Enter the output log name: " log_file
#read -p "Enter the timout for code block execution: " code_timeout

# Pre-assign the variables
kernel_name="notebook_inheritor_env"
template_file="Template_notebook_1.ipynb"
output_file="output_notbook.ipynb"
log_file="job_logger.log"
code_timeout="172800" # measured in seconds - default 600

# Run the Python script
python execute_notebook.py "$kernel_name" "$template_file" "$output_file" "$log_file" "$code_timeout"