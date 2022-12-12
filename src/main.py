#!/bin/python3
import sys
import subprocess

# Metadata
version = "1.0.9"
author = "Arkapravo Ghosh"
name = "fan-mode"

# Configuration
laptop = "ASUS VivoBook 14X Pro OLED M7400QE 1.0"
fanint = "*"
fan_name = "asus-isa-0000"
filename = sys.argv[0]


def get_fan_status():  # Get the current fan status
    try:
        debug = subprocess.getoutput(f"sensors -u {fan_name}")
        for line in debug.splitlines():
            if "fan1_input" in line:
                print(
                    "Fan Speed:", (float(line.split(":")[1].strip())), "RPM"
                )  # Print the fan speed
    except Exception as debug:
        print("N/A")
    return debug


def get_temp():  # Get the current fan temperature
    try:
        debug = subprocess.getoutput("cat /sys/class/thermal/thermal_zone*/temp")
        cnt = 0
        for line in debug.splitlines():
            print(f"Temp {cnt}:", (round((float(line) / 1000))), f"{chr(176)}C")
            cnt += 1
    except Exception as debug:
        print("N/A")
    return debug


def run_command(command, mode):  # Run a command and return the output
    debug = subprocess.getoutput(command)
    if debug == "2" or debug == "0":
        print(f"Fan mode set to {mode}.")
    elif "Permission denied" in debug:
        print("You need to run this script as root to use this option.")
    return debug


def set_fan_mode(mode):  # Set the fan mode
    if mode == "auto":  # Set the fan mode to auto
        command = f"tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon{fanint}/pwm1_enable <<< 2"
        debug = run_command(command, "auto")
    elif mode == "full":  # Set the fan mode to full speed
        command = f"tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon{fanint}/pwm1_enable <<< 0"
        debug = run_command(command, "full")
    return debug


def main():  # Main function
    debug = None
    if "--help" in sys.argv or "-h" in sys.argv:  # Help
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
    elif "--auto" in sys.argv or "-a" in sys.argv:  # Set fan mode to auto
        debug = set_fan_mode("auto")
    elif "--full" in sys.argv or "-f" in sys.argv:  # Set the fan to full speed
        debug = set_fan_mode("full")
    elif "--status" in sys.argv or "-s" in sys.argv:  # Get the fan status
        debug = get_fan_status()
        debug1 = get_temp()
    elif "--version" in sys.argv or "-v" in sys.argv:  # Print the version
        print(f"{name} version {version} created by {author}.")
    else:  # Invalid option
        print("Invalid argument. Use '-h' or '--help' for help.")
    if "-d" in sys.argv or "--debug" in sys.argv:  # Print debug information
        try:
            print("\n" + debug)
        except TypeError:
            pass
        try:
            print(debug1)
        except UnboundLocalError:
            pass


if __name__ == "__main__":  # Run the main function
    main()
