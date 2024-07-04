# K11720457
# Aral Cimcim

# Write a generator function chunks(path: str, size: int, **kwargs) 
# that yields data chunks from the file specified by path.

import os

def chunks(path: str, size:int, **kwargs):

    if not os.path.isfile(path):
        raise ValueError(f"Path {path} is not a file")
    
    if size < 1:
        raise ValueError(f"Size: {size} can not be smaller than 1")
    
    with open(path, **kwargs) as f:

        while True:
            chunk = f.read(size)
            if not chunk:
                break

            yield chunk

