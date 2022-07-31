# Given a path that represents a directory in the operating system, count the number of files that are located in the subtree that has the root of the directory.
# number of files that are located in the subtree that has as root the proposed directory.
# proposed directory as root.
# The process must create a thread for each subdirectory found.

import os, threading
import sys
from random import randint

result = 0
threads = []

def countAllFiles(lock, dir_path):
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        f = os.path.join(dir_path, path)
        if os.path.isfile(f):
            count += 1
    lock.acquire()
    global result
    result += count
    lock.release()
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 countFiles.py <path>')
        exit(1)

    lock = threading.Lock()
    for root, dirs, files in os.walk(sys.argv[1]):
        threads.append(threading.Thread(target=countAllFiles, args=(lock, root)))
        threads[-1].start()

    for thread in threads:
        thread.join()

    print(result)

def generate_random_big_directory_tree(dirname: str, range_file: list, range_directorys: list, depth: int):
    """
    Generate a random directory in tree with random files number of files and directories.
    Args:
        dirname: name of the directory where the tree will be generated.
        range_file: range of number of files in one directory.
        range_directorys: range of number of directories in one directory.
        depth: depth from the root directory.

    """
    if depth == 0:
        return
    for i in range(randint(range_file[0], range_file[1])):
        open(dirname + '/' + str(i) + '.txt', 'w').close()
    for i in range(randint(range_directorys[0], range_directorys[1])):
        dirname += '/' + str(i)
        os.mkdir(dirname)
        generate_random_big_directory_tree(dirname, range_file, range_directorys, depth - 1)
    for i in range(randint(range_file[0], range_file[1])):
        open(dirname + '/' + str(i) + '.txt', 'w').close()
    return

