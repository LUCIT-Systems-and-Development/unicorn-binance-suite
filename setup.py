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
# LUCIT Online Shop: https://shop.lucit.services/software
#
# License: LSOSL - LUCIT Synergetic Open Source License
# https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/blob/master/LICENSE
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2019-2023, LUCIT Systems and Development (https://www.lucit.tech)
# All rights reserved.

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='unicorn_binance_suite',
     version='2.0.0',
     author="LUCIT Systems and Development",
     author_email='info@lucit.tech',
     url="https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite",
     description="The UNICORN Binance Suite is a Python Meta Package of unicorn-fy, unicorn-binance-local-depth-cache, "
                 "unicorn-binance-rest-api, unicorn-binance-trailing-stop-loss and unicorn-binance-websocket-api.",
     long_description=long_description,
     long_description_content_type="text/markdown",
    license='LSOSL - LUCIT Synergetic Open Source License',
     install_requires=['unicorn-binance-websocket-api>=2.0.0', 'unicorn-binance-rest-api>=2.0.0', 'unicorn-fy>=0.13.1',
                       'unicorn-binance-local-depth-cache>=1.0.0', 'unicorn-binance-trailing-stop-loss>=1.0.0',
                       'lucit-licensing-python>=1.8.1'],
     keywords='Binance, Websocket, REST, Local Depth Cache, Trailing Stop Loss, Trading Bot, Algo Trading',
     project_urls={
        'Documentation': 'https://unicorn-binance-suite.docs.lucit.tech/',
        'Changes': 'https://unicorn-binance-suite.docs.lucit.tech/changelog.html',
        'License': 'https://unicorn-binance-suite.docs.lucit.tech/license.html',
        'Issue Tracker': 'https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/issues',
        'Wiki': 'https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/wiki',
        'Author': 'https://www.lucit.tech',
        'Chat': 'https://gitter.im/unicorn-binance-suite/unicorn-binance-suite',
        'Telegram': 'https://t.me/unicorndevs',
        'Get Support': 'https://www.lucit.tech/get-support.html',
        'LUCIT Online Shop': 'https://shop.lucit.services/software',
     },
     python_requires='>=3.7.0',
     packages=find_packages(exclude=["tools", "images", "dev", "docs", ".github"]),
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
         "Programming Language :: Python :: 3.10",
         "Programming Language :: Python :: 3.11",
         "Programming Language :: Python :: 3.12",
         "License :: Other/Proprietary License",
         'Intended Audience :: Developers',
         "Intended Audience :: Financial and Insurance Industry",
         "Intended Audience :: Information Technology",
         "Intended Audience :: Science/Research",
         "Operating System :: OS Independent",
         "Topic :: Office/Business :: Financial :: Investment",
         'Topic :: Software Development :: Libraries :: Python Modules',
     ],
)

