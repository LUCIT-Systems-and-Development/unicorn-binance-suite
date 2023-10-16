[![Get a UNICORN Binance Suite License](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/unicorn-binance-suite/master/images/logo/LUCIT-UBS-License-Offer.png)](https://shop.lucit.services)

[![Github](https://img.shields.io/badge/source-github-cbc2c8)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite)
[![GitHub Release](https://img.shields.io/github/release/LUCIT-Systems-and-Development/unicorn-binance-suite.svg?label=github)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/releases)
[![GitHub Downloads](https://img.shields.io/github/downloads/LUCIT-Systems-and-Development/unicorn-binance-suite/total?color=blue)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/releases)
[![Conda Release](https://img.shields.io/conda/vn/conda-forge/unicorn-binance-suite.svg?color=blue)](https://anaconda.org/conda-forge/unicorn-binance-suite)
[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/unicorn-binance-suite.svg?color=blue)](https://anaconda.org/conda-forge/unicorn-binance-suite)
[![PyPi Release](https://img.shields.io/pypi/v/unicorn-binance-suite?color=blue)](https://pypi.org/project/unicorn-binance-suite/)
[![PyPi Downloads](https://pepy.tech/badge/unicorn-binance-suite)](https://pepy.tech/project/unicorn-binance-suite)
[![License](https://img.shields.io/badge/license-LSOSL-blue)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/blob/master/LICENSE)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/unicorn_binance_suite.svg)](https://www.python.org/downloads/)
[![PyPI - Status](https://img.shields.io/pypi/status/unicorn_binance_suite.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/issues)
[![Azure Pipelines](https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/unicorn-binance-suite-feedstock?branchName=main)](https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=15707&branchName=main)
[![Read the Docs](https://img.shields.io/badge/read-%20docs-yellow)](https://unicorn-binance-suite.docs.lucit.tech/)
[![Read How To`s](https://img.shields.io/badge/read-%20howto-yellow)](https://medium.lucit.tech)
[![Telegram](https://img.shields.io/badge/chat-telegram-41ab8c)](https://t.me/unicorndevs)
[![Gitter](https://badges.gitter.im/unicorn-binance-suite/unicorn-binance-suite.svg)](https://gitter.im/unicorn-binance-suite/unicorn-binance-suite?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![LUCIT-UBS-Banner](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/unicorn-binance-suite/master/images/logo/LUCIT-UBS-Banner-Readme.png)](https://www.lucit.tech/unicorn-binance-suite.html)

# UNICORN Binance Suite
[Description](#description) | [Installation](#installation-and-upgrade) | [How To](#howto) | [Change Log](#change-log) | 
[Documentation](#documentation) | [Social](#social) | [Notifications](#receive-notifications) | [Bugs](#how-to-report-bugs-or-suggest-improvements) | 
[Contributing](#contributing) | [Leave a review](#you-want-to-say-thank-you) | [Leave a review](#you-want-to-say-thank-you) | 
[Disclaimer](#disclaimer) | [Commercial Support](#commercial-support)

## Description
The [`UNICORN Binance Suite`](https://www.lucit.tech/unicorn-binance-suite.html) is a collection of open source Python packages that are useful for creating
automated trading systems (bots) that connect to the Binance API.

- [`UnicornFy`](https://www.lucit.tech/unicorn-fy.html): Convert received raw data from crypto exchange API endpoints into well-formed python dictionaries. 
- [`UNICORN Binance Local Depth Cache`](https://www.lucit.tech/unicorn-binance-local-depth-cache.html): A local Binance DepthCache Manager for Python that supports multiple depth caches in one instance in a easy, fast, flexible, robust and fully-featured way. 
- [`UNICORN Binance REST API`](https://www.lucit.tech/unicorn-binance-rest-api.html): An unofficial Python API to use the Binance REST API`s (com+testnet, com-margin+testnet, com-isolated_margin+testnet, com-futures+testnet, us, tr) in a easy, fast, flexible, robust and fully-featured way.
- [`UNICORN Binance Trailing Stop Loss`](https://www.lucit.tech/unicorn-binance-trailing-stop-loss.html): A Trailing Stop Loss Python Lib and [Command Line Tool](https://www.lucit.tech/ubtsl-cli.html) as well as a [standalone version for Windows and Mac](https://www.lucit.tech/unicorn-binance-trailing-stop-loss-bot.html) that does not require an installed Python environment.
- [`UNICORN Binance WebSocket API`](https://www.lucit.tech/unicorn-binance-websocket-api.html): An unofficial Python API to use the Binance Websocket API`s (com+testnet, com-margin+testnet, com-isolated_margin+testnet, com-futures+testnet, com-coin_futures, us, tr, dex/chain+testnet) in a easy, fast, flexible, robust and fully-featured way.

If you like the project, please 
[![star](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-binance-suite/master/images/misc/star.png)](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/stargazers) it on 
[GitHub](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite)! 

## Installation and Upgrade

If you run into errors during the installation take a look [here](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/wiki/Installation).

### A wheel and a source file of the latest release with `pip` from [PyPI](https://pypi.org/project/unicorn-binance-suite/)
`python3 -m pip install unicorn-binance-suite --upgrade --force-reinstall`

The `--upgrade` flag will not update the `unicorn-binance-suite` dependencies unless you add the `--force-reinstall` flag.

### A conda package of the latest release with `conda` from [Anaconda](https://anaconda.org/conda-forge/unicorn-binance-suite) via [CONDA-FORGE](https://conda-forge.org).
`conda install -c conda-forge unicorn-binance-suite`

`conda update -c conda-forge unicorn-binance-suite`

### From source of the latest release with PIP from [Github](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite)
#### Linux, macOS, ...
Run in bash:

`pip install https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/archive/$(curl -s https://api.github.com/repos/LUCIT-Systems-and-Development/unicorn-binance-suite/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")').tar.gz --upgrade`

#### Windows
Use the below command with the version (such as 1.1.0) you determined 
[here](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/releases/latest):

`pip install https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/archive/1.1.0.tar.gz --upgrade`

### From the latest source (dev-stage) with PIP from [Github](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite)
This is not a release version and can not be considered to be stable!

`pip install https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/tarball/master --upgrade`

### [Conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), [Virtualenv](https://virtualenv.pypa.io/en/latest/) or plain [Python](https://www.python.org)
Download the [latest release](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/releases/latest) 
or the [current master branch](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/archive/master.zip)
 and use:
 
- ./environment.yml
- ./requirements.txt
- ./setup.py

## Change Log
[https://unicorn-binance-suite.docs.lucit.tech//CHANGELOG.html](https://unicorn-binance-suite.docs.lucit.tech//CHANGELOG.html)

Please look for the information in the README.md of the [responsible subrepository](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite#description).

## Documentation
- [General](https://unicorn-binance-suite.docs.lucit.tech/)

Please look for the information in the README.md of the [responsible subrepository](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite#description).

## Howto
- [Instructions about the UNICORN Binance Suite](https://medium.lucit.tech/unicorn-binance-suite/home)

## Project Homepage
[https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite)

## Wiki
[https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/wiki](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/wiki)

## Social
- [Discussions](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite/discussions)
- [https://t.me/unicorndevs](https://t.me/unicorndevs)
- [https://dev.binance.vision](https://dev.binance.vision)
- [https://community.binance.org](https://community.binance.org)

## Receive Notifications
Follow us on [Twitter](https://twitter.com/LUCIT_SysDev) or on [Facebook](https://www.facebook.com/lucit.systems.and.development) for general news about the [unicorn-binance-suite](https://www.lucit.tech/unicorn-binance-suite.html)!

Please look for the information in the README.md of the [responsible subrepository](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite#description) for spezific notifications.

## How to report Bugs or suggest Improvements?
Please look for the information in the README.md of the [responsible subrepository](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite#description).

## Contributing
Please look for the information in the README.md of the [responsible subrepository](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite#description).

## You want to say Thank You?
We hope you are enjoying using our libraries and that they are proving to be useful to you. If you have a moment, we would greatly appreciate it if you could leave us a [review on Google](https://g.page/r/CbfHlcs8BfG8EAg/review). Thank you for your support!

## Disclaimer
This project is for informational purposes only. You should not construe this information or any other material as 
legal, tax, investment, financial or other advice. Nothing contained herein constitutes a solicitation, recommendation, 
endorsement or offer by us or any third party provider to buy or sell any securities or other financial instruments in 
this or any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such 
jurisdiction.

### If you intend to use real money, use it at your own risk!

Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or liabilities 
of any kind, including but not limited to direct or indirect damages for loss of profits.

### SOCKS5 Proxy / Geoblocking
We would like to explicitly point out that in our opinion US citizens are exclusively authorized to trade on Binance.US and that this restriction must not be circumvented!

The purpose of supporting a SOCKS5 proxy in the UNICORN Binance Suite and its modules is to allow non-US citizens to use US services. For example, Github actions with UBS will not work without a SOCKS5 proxy, as they will inevitably run on servers in the US and be blocked by Binance.com. Moreover, it also seems justified that traders, data scientists and companies from the US analyze binance.com market data - as long as they do not trade there.

## Commercial Support

[![Get professional and fast support](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/unicorn-binance-suite/master/images/support/LUCIT-get-professional-and-fast-support.png)](https://www.lucit.tech/get-support.html)

***Do you need a developer, operator or consultant?*** [Contact us](https://www.lucit.tech/contact.html) for a non-binding initial consultation!
