import os, sys, getopt


def get_path(path):
    """
    Returns the directory do be described.
    """
    return os.path.abspath(path)


def get_depth(depth):
    """
    Returns an number representation of how deep the directory hierarchy
    should be described.
    """
    try:
        dpt = int(depth)
    except:
        dpt = 2

    return dpt


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


def help():
    """
    Prints help information and exits
    """
    print("TREE: Describe a path and its contents.")
    print("Usage:")
    print(" python tree.py [OPTIONS] path")
    print("Options:")
    print(" --help, -h: display this help and exit.")
    print(" --depth, -d: specifies how deep the path should be described. Default is 2.")
    sys.exit(2)


def validate_options(options, values):
    """
    Validate mandatory arguments an handle --help argument.
    Returns a pair with depth and path do describe.
    """
    depth = None

    for opt, value in options:
        if opt in ("--help", "-h"):
            help()
        elif opt in ("--depth", "-d"):
            depth = value

    depth = get_depth(depth)

    if (size := len(values)) != 1:
        print("Wrong number of arguments. 1 expected " + str(size) + " received")
        help()
    else:
        path = get_path(values[0])

    return path, depth


def handle_opts(system_arguments):
    """
    Parse system arguments and validate its options.
    Returns depth and path to describe.
    """
    unix_options = "hd:"
    allowed_options = ["help", "depth="]
    arguments = system_arguments[1:]

    try:
        opts, values = getopt.getopt(arguments, unix_options, allowed_options)
        print(opts, values)
        return validate_options(opts, values)
    except getopt.GetoptError as err:
        print(str(err))
        help()


directory, max_depth = handle_opts(sys.argv)
describe_directory(max_depth, 1, directory)
