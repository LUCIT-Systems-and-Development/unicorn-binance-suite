#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: upload_wheel.sh
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
#
# create this file:
# ~/.pypirc


python3 -m twine upload dist/*
