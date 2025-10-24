from pathlib import Path
import sys

def replace(file_path, original_word, new_word):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # print(type(lines))
        new_lines = []
        for line in lines:
            line = line.replace(original_word, new_word)
            new_lines.append(line)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)

    except Exception as e:
        print(f"an error has occured: {e}")

# if __name__ == '__main__':
#     if len(sys.argv) < 2:
#         # Exit if no files or options are provided
#         sys.exit(0)

#     # Use if/elif/else for proper argument parsing
#     if sys.argv[1] == '-r':
#         files = Path('.').rglob('*.md')
#     elif sys.argv[1] == '-d':
#         files = []
#         # Start from the third argument to get folders
#         for folder in sys.argv[2:]:
#             files.extend(Path(folder).rglob('*.md'))
#     else:
#         files = sys.argv[1:]
    
#     for file in files:
#         try:
#             print(file)
#             # replace(file, "\exist", "\exists")
#             # replace(file, "\existss", "\exists")
#             # replace(file, "\infin", "\infty")
#             # replace(file, "\R ", "\mathbb R")
#             # replace(file, "\mathbb Rightarrow", "\Rightarrow")
#             # replace(file, "\\\\", "$$ $$")
#             # # replace(file, "$$ $$", "\\\\")
#             # # replace(file, "\\N", "\mathbb N")

#         except Exception as e:
#             print(f"Error processing {file}: {e}")
#             continue


def combine_name(name_list: list):
    name = "'"
    for folder in name_list:
        name += folder.replace("/", "'/'")
        name += ' '
    name = name[:-1]
    name += "'"
    print(name)
    return name

def combine_name(name_list: list):
    name = ""
    for folder in name_list:
        name += folder
        name += ' '
    name = name[:-1]
    print(name)
    return name


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(0)

    if sys.argv[1] == '-d':
        print(sys.argv[2:])
        folder_name = combine_name(sys.argv[2:])
        files = Path(folder_name).rglob('*.md')
    else:
        file_name = combine_name(sys.argv[1:])
        files = [file_name]
    
    for file in files:
        try:
            print(file)
            replace(file, "\exist", "\exists")
            replace(file, "\existss", "\exists")
            replace(file, "\infin", "\infty")
            replace(file, "\R ", "\mathbb R")
            replace(file, "\mathbb Rightarrow", "\Rightarrow")
            replace(file, "\\\\", "$$ $$")
            # replace(file, "$$ $$", "\\\\")
            # replace(file, "\\N", "\mathbb N")

        except Exception as e:
            print(f"Error processing {file}: {e}")
            continue