#!/bin/python3
import sys
import subprocess

version = "1.0.0"
author = "Arkapravo Ghosh"
name = "fan-mode"

laptop = "ASUS VivoBook 14X Pro OLED M7400QE 1.0"
fanint = "6"
fan_name = "asus-isa-0000"
filename = sys.argv[0]

def get_fan_mode():
    try:
        debug = subprocess.getoutput(f"sensors -u {fan_name}")
        for line in debug.splitlines():
            if "fan1_input" in line:
                print(float(line.split(":")[1].strip()))
    except Exception as debug:
        return "N/A"
    return debug

def run_command(command, mode):
    debug = subprocess.getoutput(command)
    if debug == "2" or debug == "0":
        print(f"Fan mode set to {mode}.")
    elif "Permission denied" in debug:
        print("You need to run this script as root to use this option.")
    return debug

def set_fan_mode(mode):
    if mode == "auto":
        command = f"tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon{fanint}/pwm1_enable <<< 2"
        debug = run_command(command, "auto")

    elif mode == "full":
        command = f"tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon{fanint}/pwm1_enable <<< 0"
        debug = run_command(command, "full")
    return debug


def main():
    debug = None
    if "--auto" in sys.argv or "-a" in sys.argv:
        debug = set_fan_mode("auto")
    elif "--full" in sys.argv or "-f" in sys.argv:
        debug = set_fan_mode("full")
    elif "--help" in sys.argv or "-h" in sys.argv:
        print(
            f"""
Usage: {filename} [OPTION]

Set the fan mode of {laptop}.
    -a, --auto\t\t\tSet the fan mode to auto.
    -f, --full\t\t\tSet the fan mode to full speed.
    -d, --debug\t\t\tPrint debug information.
    -v, --version\t\tPrint the version of this script.
    -h, --help\t\t\tShow this help message.
"""
        )
    elif "--status" in sys.argv or "-s" in sys.argv:
        debug = get_fan_mode()
    elif "--version" in sys.argv or "-v" in sys.argv:
        print(f"{name} version {version} created by {author}.")
    else:
        print("Invalid argument. Use '-h' or '--help' for help.")
    if "-d" in sys.argv or "--debug" in sys.argv:
        print("\n" + debug)


if __name__ == "__main__":
    main()
