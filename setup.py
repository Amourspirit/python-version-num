import pathlib
import os
import sys
import platform
from setuptools import setup

MODULE_ROOT_NAME='verr'
PKG_NAME='verr'
MAJOR = 1
MINOR = 1
MICRO = 0
ISRELEASED = True
VERSION = f'{MAJOR}.{MINOR}.{MICRO}'

min_version = (3, 6, 0)


def is_right_py_version(min_py_version):
    global PKG_NAME
    if sys.version_info < (3,):
        sys.stderr.write(
            'Python 2 has reached end-of-life and is by ' + PKG_NAME)
        return False

    if sys.version_info < min_py_version:
        python_min_version_str = '.'.join((str(num) for num in min_py_version))
        no_go = f'You are using Python {platform.python_version()}. Python >={python_min_version_str} is  required.'
        sys.stderr.write(no_go)
        return False

    return True


if not is_right_py_version(min_version):
    sys.exit(-1)

# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
with open(HERE/ "README.md") as fh:
    README = fh.read()


def getListOfFiles(dir_name):
    '''
    For the given path, get the List of all files in the directory tree 
    '''
    # create a list of file and sub directories
    # names in the given directory
    list_of_files = os.listdir(dir_name)
    all_files = list()
    # Iterate over all the entries
    for entry in list_of_files:
        # Create full path
        full_path = os.path.join(dir_name, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + getListOfFiles(full_path)
        else:
            all_files.append(full_path)

    return all_files


def get_src_modules(root_path: pathlib.Path):
    global MODULE_ROOT_NAME
    dir_name = root_path / MODULE_ROOT_NAME
    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dir_name)
    _slice = len(str(dir_name)) + 1
    py_lst = [f[_slice:-3]
              for f in list(filter(lambda p: p.endswith('.py'), listOfFiles))]
    return py_lst


MODULES = get_src_modules(HERE)

# This call to setup() does all the work
setup(
    name=PKG_NAME,
    version=VERSION,
    description="Represents a version number that can be parsed and compared.",
    long_description_content_type="text/markdown",
    long_description=README,
    url="https://github.com/Amourspirit/python-version-num",
    author=":Barry-Thomas-Paul: Moss",
    author_email='bigbytetech@gmail.com',
    license="MIT",
    packages=[MODULE_ROOT_NAME],
    py_modules=MODULES,
    keywords=['python', 'version', 'verr'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=True,
)
