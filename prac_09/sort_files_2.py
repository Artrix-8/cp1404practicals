import os
import shutil

os.chdir("FilesToSort")
extension_to_directory = {}
for filename in os.listdir('.'):
    extension = filename.split('.')[-1]
    if extension not in extension_to_directory:
        directory = input(f"What category would you like to sort {extension} files into? ")
        extension_to_directory[extension] = directory
    try:
        os.mkdir(directory)
    except FileExistsError:
        pass
    shutil.move(filename, extension_to_directory[extension])
