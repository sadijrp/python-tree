import os
import sys


def get_path():
    """
    Returns the directory do be described.
    """
    if len(sys.argv) < 2:
        path = os.getcwd()
    else:
        path = os.path.abspath(sys.argv[1])

    return path


current_directory = get_path()
try:
    directory_elements = os.listdir(current_directory)
    for element in directory_elements:
        print("-" + element)
except FileNotFoundError:
    print("Cannot find specified path.")
