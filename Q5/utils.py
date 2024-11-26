import os
from pathlib import Path

class FileUtils:

    def list_filenames(self, input_path):
        return os.listdir(input_path)

    def read_input(self, filename):
        content = self.parse_file(filename)
        alpha_statement = content[0]
        KB_size = content[1]
        KB = content[2:]
        return KB, alpha_statement

    def parse_file(self, filename):
        content = []
        with open(filename, 'r') as f:
            content= f.read().splitlines()
        return content

    def write_output(self, result, check, filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as f:
            for loop_res in result:
                f.write(str(len(loop_res)) + '\n')
                for clause in loop_res:
                    string = ''
                    for c in clause:
                        string += c
                        if c != clause[-1]:
                            string += ' OR '
                    f.write(string + '\n')
            if check:
                f.write('YES')
            else:
                f.write('NO')
