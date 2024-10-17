# asus-fan-mode

Fan Mode Control for Asus Vivobook 14X Pro OLED in Linux.

![](https://img.shields.io/github/license/Arkapravo-Ghosh/asus-fan-mode)
![](https://img.shields.io/badge/platform-Linux-blue)

## Installation

Installation Guide is written in [INSTALLATION.md](INSTALLATION.md).

## Usage

- `sudo fan-mode --auto` to automatically optimise fan speed as per usage
- `sudo fan-mode --full` to force fan to run in full speed
- `fan-mode --status` to get fan status
- `fan-mode --setup` to generate a default configuration file
- `fan-mode --help` for more information

## Make Options

- `help` to show help message
- `check` to check for build dependencies
- `clean` to clean all the build artifacts
- `build` to build the executable
- `install` to install the program
- `remove` to remove the program

## Known Issues

- GPU Fan Controlling is not supported yet.
