# asus-fan-mode
Fan Mode Control for Asus Vivobook 14X Pro OLED in Linux

![](https://img.shields.io/github/license/Arkapravo-Ghosh/asus-fan-mode)
![](https://img.shields.io/badge/platform-Linux-blue)

* [Click Here](src/main.py) for Source code.
## Installation
> Installation Guide is written in [INSTALLATION.md](INSTALLATION.md).
## Usage
* `sudo fan-mode --auto` - Automatically optimise fan speed as per usage
* `sudo fan-mode --full` - Force fan to run in full speed
* `fan-mode --status` - Get status of fan
* `fan-mode --setup` - To generate a default configuration file
> Use `fan-mode --help` for more information.
## Misc
* [`clean.sh`](clean.sh) - Execute this script to automatically clean all build files created while compiling or installing the project. This does not uninstall the program.
* [`compile.sh`](compile.sh) - Execute this script to automatically compile the project. This does not install the program.
> NOTE: Please run `sudo pip3 install -r requirements.txt` in the repo directory before using this script if you have not installed the dependencies of this project yet.

