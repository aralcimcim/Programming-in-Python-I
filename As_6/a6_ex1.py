# K11720457
# Aral Cimcim

# Write a function file_statistics(path: str) that prints the statistics of a given file.

import os

def file_statistics(path: str):

    if not os.path.exists(path):
        raise OSError(f"Path {path} does not exist")
    
    if not path.endswith(".txt"):
        raise ValueError(f"{path} is not a text file")
    
    with open(path, "r", encoding="utf8") as f:
        content = f.read()
        num_lines = content.split("\n")

        if num_lines[-1] == "":
            num_lines.pop()

        num_words = content.split()
        num_chars = len(content)

        num_digits = 0
        for char in content:
            if char.isdigit():
                num_digits += 1

        print("--------------------")
        print(f"Statistics of file {os.path.basename(path)}: ")
        print(f"Number of lines: {len(num_lines)}")
        print(f"Number of words: {len(num_words)}")
        print(f"Number of characters: {num_chars}")
        print(f"Number of digits: {num_digits}")
        print("--------------------")

