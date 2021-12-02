import sys
import os
import os.path
import logging


def add_sep(cur_path):
    if not cur_path.endswith(os.sep):
        return cur_path + os.sep


def make_paths_relative(cur_dir):
    cur_dir = add_sep(cur_dir)
    filename = os.path.join(cur_dir, 'lsrm.cnf')
    with open(filename) as f:
        lines = f.readlines()

    with open(filename, 'w') as g:
        for line in lines:
            line = line.rstrip()
            if not line or line.startswith('[') or '=' not in line:
                g.write(line + '\n')
                continue
            
            name, value = [word.strip() for word in line.split('=', 1)]
            if 'Descriptor' not in name and value.lower().startswith(cur_dir.lower()):
                old_value = value
                value = value[len(cur_dir):] if len(value) > len(cur_dir) else ''
                logging.info(f'config={cur_dir}: changed {name} from {old_value} to {value}')
            g.write(f'{name}={value}\n')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    init_dir = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.getcwd()
    for cur_dir, sub_dirs, files in os.walk(init_dir):
        if 'lsrm.cnf' not in files:
            continue
        make_paths_relative(cur_dir)
    
