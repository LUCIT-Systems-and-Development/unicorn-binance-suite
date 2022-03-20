#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: setup.py
#
# Part of ‘UNICORN Binance Suite’
# Project website: https://www.lucit.tech/unicorn-binance-suite.html
# Github: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite
# Documentation: https://unicorn-binance-suite.docs.lucit.tech
# PyPI: https://pypi.org/project/unicorn-binance-suite
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2022-2022, LUCIT Systems and Development (https://www.lucit.tech) and Oliver Zehentleitner
# # All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='unicorn-binance-suite',
     version='1.0.2',
     author="LUCIT Systems and Development",
     author_email='info@lucit.tech',
     url="https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite",
     description="The UNICORN Binance Suite is a Python Meta Package of unicorn-fy, unicorn-binance-local-depth-cache, "
                 "unicorn-binance-rest-api and unicorn-binance-websocket-api.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='MIT License',
     install_requires=['unicorn-binance-websocket-api', 'unicorn-binance-rest-api', 'unicorn-fy',
                       'unicorn-binance-local-depth-cache'],
     keywords='',
     project_urls={
        'Documentation': 'https://unicorn-binance-suite.docs.lucit.tech/',
        'Changes': 'https://unicorn-binance-suite.docs.lucit.tech//CHANGELOG.html',
        'Issue Tracker': 'https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/issues',
        'Wiki': 'https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/wiki',
        'Author': 'https://www.lucit.tech',
        'Chat': 'https://t.me/unicorndevs',
     },
     python_requires='>=3.7.0',
     packages=setuptools.find_packages(exclude=["tools", "images", "pypi", "sphinx", "docs", ".github"]),
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
         "Programming Language :: Python :: 3.10",
         "License :: OSI Approved :: MIT License",
         'Intended Audience :: Developers',
         "Intended Audience :: Financial and Insurance Industry",
         "Intended Audience :: Information Technology",
         "Intended Audience :: Science/Research",
         "Operating System :: OS Independent",
         "Topic :: Office/Business :: Financial :: Investment",
         'Topic :: Software Development :: Libraries :: Python Modules',
     ],
)

