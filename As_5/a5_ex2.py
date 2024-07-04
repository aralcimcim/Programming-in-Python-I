# K11720457
# Aral Cimcim

# Write a function print_directory(dir_path: str) that enumerates and prints recursively all files and sub directories in an input directory specified by its path dir_path.

import os

def print_directory(dir_path: str):

    # If dir_path is a path to a file, print  "dir_path is a file not a directory".
    if os.path.isfile(dir_path):
        print(f"{dir_path} is a file not a directory")
    
    # If dir_path is a path to a directory, enumerate and print recursively the input directory and all its files and sub directories.
    elif os.path.isdir(dir_path):
        
        # Print the root folder dir.
        print(dir_path)

        # Iterate through the sub_dirs.
        for content in os.listdir(dir_path):
            print_directory_recursively(os.path.join(dir_path, content), level = 1)

    # Otherwise print "dir_path is invalid".
    else:
        print(f"{dir_path} is invalid")

def print_directory_recursively(dir_path: str, level: int):

    # Set tab length per level.
    tab = '    ' * level

    # If path is a directory print its contents.
    if os.path.isdir(dir_path):
        print(f"{tab}{os.path.basename(dir_path)}")
        for content in os.listdir(dir_path):
            print_directory_recursively(os.path.join(dir_path, content), level + 1)

    # If path is a file print its contents.
    elif os.path.isfile(dir_path):
        print(f"{tab}{os.path.basename(dir_path)}")

