import os
import sys
import logging
from tqdm import tqdm
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import CellExecutionError

def execute_notebook(kernel_name, template_file, output_file, log_file, code_timeout):
    # Configure logging
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt="%Y-%m-%d %H:%M:%S", filemode='w+')

    try:
        # Read in the template notebook
        print('Reading in template notebook 📓')
        with open(template_file) as f:
            nb = nbformat.read(f, as_version=4)

        # Extract the code blocks from the template notebook
        print('Extracting code blocks from notebook 📝')
        code_blocks = []
        for cell in nb.cells:
            if cell.cell_type == 'code':
                code_blocks.append(cell.source)

        # Execute the code blocks in a new notebook
        print('Executing code blocks 🔨')
        ep = ExecutePreprocessor(timeout=code_timeout, kernel_name=kernel_name)
        new_nb = nbformat.v4.new_notebook()
        
        
        counter = 1
        for i, block in enumerate(tqdm(code_blocks, desc="Executing Code Blocks")):
            new_nb.cells.append(nbformat.v4.new_code_cell(block))

            # Execute the code in the new notebook
            try:
                logging.info('Executing code block {}...'.format(i + 1))
                output, resources = ep.preprocess(new_nb, {'metadata': {'path': '.'}})
                
            except CellExecutionError:
                out = None
                msg = 'Error executing the notebook "%s".\n\n' % template_file
                msg += 'See notebook "%s" for the traceback.' % output_file
                print(msg)
                logging.exception(msg)
                raise

            # Check for the presence of the 'save_checkpoint' variable in the code block
            checkpoint_variable = 'save_checkpoint = True'
            if checkpoint_variable in block:
                partial_output_file = f'{os.path.splitext(output_file)[0]}_partial_{counter}.ipynb'
                counter+= 1
                with open(partial_output_file, mode='w', encoding='utf-8') as f:
                    nbformat.write(new_nb, f)

                logging.info('Partial notebook saved at code block {} to {}'.format(i + 1, partial_output_file))

    
    except Exception as e:
        msg = 'Error: {}'.format(e)
        logging.error(msg)
        print(msg)
        logging.exception(e)
        print('Error has occured not due to code block (ﾒ﹏ﾒ)')
        raise
        
     
    finally:
        # Save the final executed notebook with outputs
        with open(output_file, mode='w', encoding='utf-8') as f:
            nbformat.write(new_nb, f)
        
 
    # If successful inform user 
    print('Executing code blocks complete ╰(▔∀▔)╯')
    logging.info('Successfully executed and saved final notebook to {}'.format(output_file))

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python execute_notebook.py <kernel_name> <template_file> <output_file> <log_file> <code_timeout>")
        sys.exit(1)

    kernel_name = sys.argv[1]
    template_file = sys.argv[2]
    output_file = sys.argv[3]
    log_file = sys.argv[4]
    code_timeout = int(sys.argv[5])

    execute_notebook(kernel_name, template_file, output_file, log_file, code_timeout)
