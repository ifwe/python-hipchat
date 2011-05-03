#!/usr/bin/env python                                                                                                                                           

from setuptools import setup, find_packages

setup(
    name = "hipchat",
    version = "0.0.1",
    packages = find_packages(),

    author = "Yaakov M Nemoy",
    author_email = "loup@hexago.nl",
    description = "Pythonic interface on top of HipChat RPC",
    license = "WTFPL",

    entry_points = {
        'console_scripts': [
            ]
        },
    )
