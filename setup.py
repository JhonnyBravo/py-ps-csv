#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except Exception:
    long_description = ""

setup(
    name="py-ps-csv",
    version="1.0",
    description="Utilities for csv files.",
    author="Jhonny Bravo",
    author_email="sanfranceshika5@gmail.com",
    url="https://github.com/JhonnyBravo/py-ps-csv.git",
    packages=find_packages(),
    long_description=long_description,
    entry_points={
        "console_scripts": [
            "add_csv_record=ps_csv.bin.add_csv_record:main",
            "get_csv_record=ps_csv.bin.get_csv_record:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
