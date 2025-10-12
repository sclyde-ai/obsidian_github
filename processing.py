import os
import re
from pathlib import Path
import sys

def remove_empty_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        non_empty_lines = [line for line in lines if line.strip()]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(non_empty_lines)

    except Exception as e:
        print(f"an error has occured: {e}")

def remove_end_indnet(file_path):
    with open(file_path, 'rb+') as f:
        try:
            f.seek(-1, os.SEEK_END)
        except OSError:
            print("the file_path is empty")
            exit()

        if f.read(1) == b'\n':
            f.seek(-1, os.SEEK_END)
            f.truncate()

def count_leading_spaces(file_path) -> list:
    try:
        spaces_numbers = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                leading_spaces = len(line.rstrip('\n')) - len(line.lstrip(' ')) +1
                spaces_numbers.append(leading_spaces)
        return spaces_numbers
    except Exception as e:
        print(f"an error has occured: {e}")
        return None

def remove_leading_spaces(file_path, num_chars):
    try:
        lines = []
        with open(file_path, 'r', encoding='utf-8') as f_in:
            for line in f_in:
                print(line)
                lines.append(line[num_chars:])
        
        with open(file_path, 'w', encoding='utf-8') as f_out:
            for line in lines:
                f_out.write(line)
    except Exception as e:
        print(f"an error has occured: {e}")

def processing_files(files: list):
    for file in files:
        try:
            print(file)
            remove_empty_lines(file)
            numbers_of_spaces = count_leading_spaces(file)
            min_number = min(numbers_of_spaces)
            remove_leading_spaces(file, min_number)
        except:
            continue

if __name__ == '__main__':

    if '-r' in sys.argv[1]:
        files = Path('.').rglob('*.md')
    if '-d' in sys.argv[1]:
        files = []
        for folder in sys.argv[1:]:
            files = Path(folder).rglob('*.md')
    else:
        files = sys.argv[1:]
    
    processing_files(files)
