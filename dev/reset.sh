#!/usr/bin/bash

rm *.log
rm dev/*.log

rm build -r
rm dist -r
rm *.egg-info -r

rm unicorn_binance_suite/*.c
rm unicorn_binance_suite/*.html
rm unicorn_binance_suite/*.dll
rm unicorn_binance_suite/*.so

rm .print_summary.txt