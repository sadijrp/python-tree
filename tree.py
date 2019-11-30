import os


current_directory = os.getcwd()
directory_elements = os.listdir(current_directory)

for element in directory_elements:
    print("-" + element)
