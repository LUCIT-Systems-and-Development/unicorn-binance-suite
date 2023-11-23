#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: dev/pypi/create_wheel.sh
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


security-check() {
    echo -n "Did you change the version in \`CHANGELOG.md\` and used \`dev/set_version.py\`? [yes|NO] "
    local SURE
    read SURE
    if [ "$SURE" != "yes" ]; then
        exit 1
    fi
    echo "https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/actions/workflows/build_wheels.yml"
    echo "https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/actions/workflows/build_conda.yml"
}

compile-check() {
    echo -n "Compile local? [yes|NO] "
    local SURE
    read SURE
    if [ "$SURE" != "yes" ]; then
        exit 1
    fi
    echo "ok, lets go ..."
    python3 setup.py sdist
}

security-check
compile-check
