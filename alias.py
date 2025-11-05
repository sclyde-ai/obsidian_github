import os
from pathlib import Path
import sys
import subprocess
import re

def add_head(file_path, head_list):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # print(lines)
        lines = head_list + lines

        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)

    except Exception as e:
        print(f"an error has occured: {e}")

def make_alias(file_path, alias_list):
    try:
        head_list = []
        head_list.append("---\n")
        head_list.append("alias:\n")
        head_list.append(f"    {alias_list}\n")
        head_list.append("---\n")
        # print(head_list)
        add_head(file_path, head_list)

    except Exception as e:
        print(f"an error has occured: {e}")

import string

alpha_lower = list(string.ascii_lowercase)
alpha_upper = list(string.ascii_uppercase)

hiragana = [chr(i) for i in range(0x3040, 0x30A0)]

katakana = [chr(i) for i in range(0x30A0, 0x3100)]

kanji_common = [chr(i) for i in range(0x4E00, 0xA000)]


# 辞書（dict）の作成
unicode_dict = {
    'hiragana': hiragana,
    'katakana': katakana,
    'kanji_common': kanji_common,
    'alpha_lower': alpha_lower,
    'alpha_upper': alpha_upper,
}


def convert_file_name_to_alias(file_path):
    file_name = os.path.basename(file_path)
    if file_name[0] == '_':
        file_name = file_name[1:]
    file_name_split = re.split(r'[., •]', file_name)
    # print(file_name_split)
    file_name_split = file_name_split[:-1]
    file_name_split = [x for x in file_name_split if x != '']
    # print(file_name_split)
    alias_list = []

    alias = file_name_split[0]
    for i in range(1, len(file_name_split)):
        if any(char in file_name_split[i] for char in alpha_lower) and any(char in file_name_split[i-1] for char in alpha_lower):
            alias += ' ' + file_name_split[i]
            # print(alias)
        else:
            alias_list.append(alias)
            alias = ""
            alias = file_name_split[i]
            # print(alias)
    alias_list.append(alias)
    return alias_list

if __name__ == "__main__":
    try:
        subprocess.run(
            ["git", "pull"], 
            capture_output=True,
            text=True, 
            check=True
        )
    except Exception as e:
        print(f"an error has occured: {e}")

    print(sys.argv)
    
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
            alias_list = convert_file_name_to_alias(file)
            make_alias(file, alias_list)
            print(alias_list)
        except Exception as e:
            print(f"Error processing {file}: {e}")
            continue
