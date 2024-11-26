import os
import resolution
import utils

# INPUT_DIR = '.\Q5\input\\'
# OUTPUT_DIR = '.\Q5\output\\'
INPUT_DIR = '.\Q5\input_rp\\'
OUTPUT_DIR = '.\Q5\output_rp\\'

file_utils = utils.FileUtils()
resolution = resolution.Resolution()

filenames = file_utils.list_filenames(INPUT_DIR)

for filename in filenames:
    KB, alpha_statement = file_utils.read_input(INPUT_DIR + filename)
    result, check = resolution.pl_resolution(KB, alpha_statement)
    file_utils.write_output(result, check, OUTPUT_DIR + 'output' + '-' + filename)