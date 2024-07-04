import re
import os

def search_file():
    file_name = input("Enter file name: ")
    if not os.path.isfile(file_name):
        raise ValueError(f"'{file_name}' is not a file.")
    
    encoding = input("Enter character encoding or press ENTER for default (utf-8): ")
    if encoding == "":
        encoding = "utf-8"
    
    with open(file_name, "r", encoding=encoding) as f:
        user_data = f.read()
    
    while True:
        pattern = input("Enter pattern or press ENTER to exit: ")
        if pattern == "":
            break

        list_of_matches = re.findall(pattern, user_data)
        print(f"{pattern}: {list_of_matches}")

search_file()