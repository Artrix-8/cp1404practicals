"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")

    new_name = ""
    for index, character in enumerate(filename):
        try:
            if character.islower() and filename[index-1] == '_':
                new_name += character.upper()
            elif character.islower() and filename[index-1] == '(':
                new_name += character.upper()
            elif not new_name:
                new_name += character.upper()
            else:
                new_name += character
            if character.islower() and filename[index+1].isupper():
                new_name += '_'
            if character.islower() and filename[index+1] == '(':
                new_name += '_'
            if character.isupper() and filename[index + 1].isupper():
                new_name += '_'
        except IndexError:
            pass
    print(new_name)
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        """
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        """

        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)


demo_walk()
