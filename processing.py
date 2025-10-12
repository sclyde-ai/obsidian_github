import os
import re
from pathlib import Path
import sys

def remove_empty_lines(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        non_empty_lines = [line for line in lines if line.strip()]

        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(non_empty_lines)

    except Exception as e:
        print(f"an error has occured: {e}")

def remove_end_indnet(file_path):
    with open(file_path, 'rb+') as f:
        try:
            f.seek(-1, os.SEEK_END)
        except OSError:
            print("the file is empty")
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

def remove_leading_spaces(file, num_chars):
    try:
        lines = []
        with open(file, 'r', encoding='utf-8') as f_in:
            for line in f_in:
                print(line)
                lines.append(line[num_chars:])
        
        with open(file, 'w', encoding='utf-8') as f_out:
            for line in lines:
                f_out.write(line)
    except Exception as e:
        print(f"an error has occured: {e}")

if __name__ == '__main__':

    if sys.argv[1] == '-r':
        md_files = Path('.').rglob('*.md')
    else:
        md_files = sys.argv[1:]

    for file in md_files:
        try:
            print(file)
            remove_empty_lines(file)
            numbers_of_spaces = count_leading_spaces(file)
            min_number = min(numbers_of_spaces)
            remove_leading_spaces(file, min_number)
        except:
            continue