#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: unittest_binance_suite.py
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

import unicorn_binance_suite
import logging
import unittest
import os

import tracemalloc
tracemalloc.start(25)

logging.getLogger("unicorn_binance_websocket_api")
logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")

print(f"Starting unittests!")


class Suite(unittest.TestCase):
    def test_get_name(self):
        print(unicorn_binance_suite.manager.__app_name__)

    def test_get_version(self):
        print(unicorn_binance_suite.manager.__version__)


if __name__ == '__main__':
    unittest.main()
