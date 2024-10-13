# asus-fan-mode

Fan Mode Control for Asus Vivobook 14X Pro OLED in Linux

![](https://img.shields.io/github/license/Arkapravo-Ghosh/asus-fan-mode)
![](https://img.shields.io/badge/platform-Linux-blue)

- [Click Here](src/main.py) for Source code.

## Installation

> Installation Guide is written in [INSTALLATION.md](INSTALLATION.md).

## Usage

- `sudo fan-mode --auto` - Automatically optimise fan speed as per usage
- `sudo fan-mode --full` - Force fan to run in full speed
- `fan-mode --status` - Get status of fan
- `fan-mode --setup` - To generate a default configuration file
- `fan-mode --help` for more information.

## Disabling Automatic Recovery of Fan Mode on Reboot

- `sudo systemctl disable --now fan-mode-recovery`

## Make Options

- **clean** - Clean all the build artifacts.
- **compile** - Compile the program.
- **install** - Install the program.
- **remove** - Remove the program.
- **check** - Check for required tools.

### Known Issues

- GPU Fan Controlling is not supported yet.
