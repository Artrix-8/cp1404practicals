import os
import shutil

os.chdir("FilesToSort")
for filename in os.listdir('.'):
    directory = filename.split('.')[-1]
    try:
        os.mkdir(directory)
    except FileExistsError:
        pass
    shutil.move(filename, directory)
