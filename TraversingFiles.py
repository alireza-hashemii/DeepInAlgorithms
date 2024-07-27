from os import listdir
from os.path import isfile, join
from collections import deque


def print_names(start_dir):
    search_deque = deque()
    search_deque.append(start_dir)

    while search_deque:
        direc = search_deque.popleft()
        for file in sorted(listdir(direc)):
            fulldir = join(direc, file)
            if isfile(fulldir):
                print(file)
            else: 
                search_deque.append(fulldir)
                
print_names(r"c:\Users\AVA\Desktop\must-read")