import os
from pathlib import Path
import sys
import subprocess

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
            # This happens on an empty file, which is fine.
            return

        if f.read(1) == b'\n':
            f.seek(-1, os.SEEK_END)
            f.truncate()

def count_leading_spaces(file_path):
    try:
        spaces_numbers = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                leading_spaces = 0
                for char in line:
                    if char == ' ':
                        leading_spaces += 1
                    if char != ' ':
                        break
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
                lines.append(line[num_chars:])
        
        with open(file_path, 'w', encoding='utf-8') as f_out:
            f_out.writelines(lines)
    except Exception as e:
        print(f"an error has occured: {e}")

if __name__ == '__main__':
    try:
        result = subprocess.run(
            ["git", "pull"], 
            capture_output=True, 
            text=True, 
            check=True
        )
    except Exception as e:
        print(f"an error has occured: {e}")
    
    if len(sys.argv) < 2:
        # Exit if no files or options are provided
        sys.exit(0)

    # Use if/elif/else for proper argument parsing
    if sys.argv[1] == '-r':
        files = Path('.').rglob('*.md')
    elif sys.argv[1] == '-d':
        files = []
        # Start from the third argument to get folders
        for folder in sys.argv[2:]:
            files.extend(Path(folder).rglob('*.md'))
    else:
        files = sys.argv[1:]
    
    for file in files:
        try:
            print(file)
            remove_empty_lines(file)
            numbers_of_spaces = count_leading_spaces(file)
            if numbers_of_spaces: # Check if list is not empty
                min_number = min(numbers_of_spaces)
                remove_leading_spaces(file, min_number)
        except Exception as e:
            print(f"Error processing {file}: {e}")
            continue