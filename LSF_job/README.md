# Notebook inheritor LSF job
---
This folder holds examples of how to use the notebook inheritor script from a bash script for a LSF job


## Examples

- Example 1:
    - Run as a job using a bash script to a LSF
    - Note the environment needs to be activated for LSF

## Instructions to execute 

1. Move into the directory holding the execute_notebook.py, run_execute_notebook.sh and the notebook to inherit

```
cd path/to/directory/holding/files

```

2. Open execute_notebook.py script and update with parameters of interest


3. Ensure the shell script has correct permissions

```
chmod 755 run_execute_notebook.sh

chmod 755 run_job.sh
```

4. Activate the virtual environment

```
conda activate notebook_inheritor_env

```


5. Run the shell script from command line

```
./run_job.sh

```
