import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="version-comp",
    version="0.1.0",
    description="Represents a version number",
    long_description_content_type="text/markdown",
    long_description=README,
    url="https://github.com/Amourspirit/python-version-num",
    author=":Barry-Thomas-Paul: Moss",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["version"],
    include_package_data=True,
)
