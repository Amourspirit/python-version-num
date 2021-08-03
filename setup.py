import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
with open(HERE/ "README.md") as fh:
    README = fh.read()

# This call to setup() does all the work
setup(
    name="verr",
    version="0.1.3",
    description="Represents a version number that can be parsed and compared.",
    long_description_content_type="text/markdown",
    long_description=README,
    url="https://github.com/Amourspirit/python-version-num",
    author=":Barry-Thomas-Paul: Moss",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=['verr'],
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
