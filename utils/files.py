from os.path import dirname
from os.path import join
print(__file__)
MAIN_DIRECTORY = dirname(dirname(__file__))
def get_full_path(*path):
    return join(MAIN_DIRECTORY, *path)