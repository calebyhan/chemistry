# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="chemistry_ch",
    version="0.1.4",
    description="Python library for chemistry equations and formulas.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/calebyhan/chemistry",
    author="Caleb Han",
    author_email="calebhantech@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(
        where='src'
    ),
    package_dir={"":"src"},
    include_package_data=True
)