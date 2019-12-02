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


def get_depth():
    """
    Returns an number representation of how deep the directory hierarchy
    should be described.
    """
    try:
        depth = sys.argv[2]
    except IndexError:
        depth = 2

    return int(depth)


def print_directory_element(depth, element):
    """
    Prints the specified element with depth blank spaces
    """
    print(depth*2*" " + "- " + element)


def describe_directory(max_depth, current_depth, path):
    """
    Roam specified directory describing it's elements.
    """
    if current_depth == max_depth:
        return
    try:
        for element in os.listdir(path):
            print_directory_element(current_depth, element)
            next_path = os.path.join(path, element)
            if os.path.isdir(os.path.join(path, element)):
                describe_directory(max_depth, current_depth+1, next_path)
    except FileNotFoundError:
        print("Cannot find specified path.")


current_directory = get_path()
max_depth = get_depth()
describe_directory(max_depth, 1, current_directory)
