# Notebook inheritor not in activated environment
---
This folder holds examples of how to use the notebook inheritor script when not in an activated environemnt


## Examples

- Example 1:
    - Basic implementation
    
    
- Example 2:
    - Include checkpoints for notebook outputs
    - Usefull for notebooks which will take a long time to run and want to see output partway without stopping run

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

4. Run the shell script from command line

```
./run_execute_notebook.sh

```