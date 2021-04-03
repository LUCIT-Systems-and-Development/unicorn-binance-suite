[![Telegram](https://img.shields.io/badge/chat-telegram-yellow.svg)](https://t.me/unicorndevs)
[![Donations/week](http://img.shields.io/liberapay/receives/oliver-zehentleitner.svg?logo=liberapay)](https://liberapay.com/oliver-zehentleitner/donate)
[![Patrons](http://img.shields.io/liberapay/patrons/oliver-zehentleitner.svg?logo=liberapay)](https://liberapay.com/oliver-zehentleitner/donate)

# UNICORN Binance Suite

[Description](#description) | [Installation](#installation-and-upgrade) |
[Documentation](#documentation) | [Social](#social) |
[Notifications](#receive-notifications) | [Bugs](#how-to-report-bugs-or-suggest-improvements) | 
[Contributing](#contributing) | [Commercial Support](#commercial-support) | [Donate](#donate)

## Description
The `UNICORN Binance Suite` is a Python Meta Package of
- [unicorn-binance-rest-api](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api)
- [unicorn-binance-websocket-api](https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api)
- [unicorn-fy](https://github.com/oliver-zehentleitner/unicorn-fy)

## Installation and Upgrade
The current dependencies are listed 
[here](https://github.com/oliver-zehentleitner/unicorn-binance-suite/blob/master/requirements.txt).

If you run into errors during the installation take a look [here](https://github.com/oliver-zehentleitner/unicorn-binance-suite/wiki/Installation).

### A wheel of the latest release with PIP from [PyPI](https://pypi.org/project/unicorn-binance-suite/)
`pip install unicorn-binance-suite --upgrade`
### From source of the latest release with PIP from [Github](https://github.com/oliver-zehentleitner/unicorn-binance-suite)
#### Linux, macOS, ...
Run in bash:

`pip install https://github.com/oliver-zehentleitner/unicorn-binance-suite/archive/$(curl -s https://api.github.com/repos/oliver-zehentleitner/unicorn-binance-suite/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")').tar.gz --upgrade`
#### Windows
Use the below command with the version (such as 1.27.0) you determined 
[here](https://github.com/oliver-zehentleitner/unicorn-binance-suite/releases/latest):

`pip install https://github.com/oliver-zehentleitner/unicorn-binance-suite/archive/1.27.0.tar.gz --upgrade`
### From the latest source (dev-stage) with PIP from [Github](https://github.com/oliver-zehentleitner/unicorn-binance-suite)
This is not a release version and can not be considered to be stable!

`pip install https://github.com/oliver-zehentleitner/unicorn-binance-suite/tarball/master --upgrade`

### [Conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), [Virtualenv](https://virtualenv.pypa.io/en/latest/) or plain [Python](https://docs.python.org/2/install/)
Download the [latest release](https://github.com/oliver-zehentleitner/unicorn-binance-suite/releases/latest) 
or the [current master branch](https://github.com/oliver-zehentleitner/unicorn-binance-suite/archive/master.zip)
 and use:
- ./environment.yml
- ./requirements.txt
- ./setup.py

## Change Log
[https://oliver-zehentleitner.github.io/unicorn-binance-suite/CHANGELOG.html](https://oliver-zehentleitner.github.io/unicorn-binance-suite/CHANGELOG.html)

## Documentation
- [General](https://oliver-zehentleitner.github.io/unicorn-binance-suite)
- [Modules](https://oliver-zehentleitner.github.io/unicorn-binance-suite/unicorn_binance_websocket_api.html)

## Examples

## Howto

## Project Homepage
[https://github.com/oliver-zehentleitner/unicorn-binance-suite](https://github.com/oliver-zehentleitner/unicorn-binance-suite)

## Wiki
[https://github.com/oliver-zehentleitner/unicorn-binance-suite/wiki](https://github.com/oliver-zehentleitner/unicorn-binance-suite/wiki)

## Social
- [https://t.me/unicorndevs](https://t.me/unicorndevs)
- [https://dev.binance.vision](https://dev.binance.vision)
- [https://community.binance.org](https://community.binance.org)

## How to report Bugs or suggest Improvements?
[List of planned features](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement) - 
click ![thumbs-up](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-rest-api/master/images/misc/thumbup.png) if you need one of them or suggest a new feature!

Before you report a bug, [try the latest release](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api#installation-and-upgrade). If the issue still exists, provide the error trace, OS 
and Python version and explain how to reproduce the error. A demo script is appreciated.

If you dont find an issue related to your topic, please open a new [issue](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/issues)!

[Report a security bug!](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/security/policy)

## Contributing
[UNICORN Binance Suite](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api) is an open 
source project which welcomes contributions which can be anything from simple documentation fixes and reporting dead links to new features. To 
contribute follow 
[this guide](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/blob/master/CONTRIBUTING.md).
 
### Contributors
[![Contributors](https://contributors-img.web.app/image?repo=oliver-zehentleitner/unicorn-binance-rest-api)](https://github.com/oliver-zehentleitner/unicorn-binance-rest-api/graphs/contributors)

We ![love](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-binance-rest-api/master/images/misc/heart.png) open source!

## Commercial Support
Need a Python developer or consulting? 

Contact [me](https://about.me/oliver-zehentleitner) for a non-binding and free consultation via my company 
[LUCIT](https://www.lucit.dev) from Vienna (Austria).

### Donate
Since you are probably a developer yourself, you will understand very well that the creation of open source software is 
not free - it requires technical knowledge, a lot of time and also financial expenditure.

If you would like to help me to dedicate my time and energy to this project, even small donations are very welcome.

[![Donate using Liberapay](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/oliver-zehentleitner/donate)

```
BTC: 39fS74fvcGnmEk8JUV8bG6P1wkdH29GtsA
LUNA: terra1ncjg4a59x2pgvqy9qjyqprlj8lrwshm0wleht5 (Memo: 108157985)
DASH: XsRhBuPkXGF9WvifdpkVhTGSmVT4VcuQZ7
ETH: 0x1C15857Bf1E18D122dDd1E536705748aa529fc9C
LTC: LYNzHMFUbee3siyHvNCPaCjqXxjyq8YRGJ
XMR: 85dzsTRh6GRPGVSJoUbFDwAf9uwwAdim1HFpiGshLeKHgj2hVqKtYVPXMZvudioLsuLS1AegkUiQ12jwReRwWcFvF7kDAbF
ZEC: t1WvQMPJMriGWD9qkZGDdE9tTJaawvmsBie
```
