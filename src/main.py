#!/bin/python3
import sys
import subprocess
import configparser

# Metadata
version = "1.1.8"
author = "Arkapravo Ghosh"
name = "fan-mode"

# Configuration
filename = sys.argv[0]
config = configparser.ConfigParser()


def get_config(conf_list):  # Fetch the configuration from the config file
    fetched_config = []
    for config_item in conf_list:
        try:
            config_item = config.get("fan-mode", config_item)
        except configparser.NoOptionError:
            print(
                f'Configuration file does not have a value for the property "{config_item}". Please run "fan-mode --setup" to create one. Use "fan-mode --help" for more information.'
            )
            sys.exit(1)
        fetched_config.append(config_item)
    return fetched_config


def run_checks():  # Run checks to see if the configuration file exists and has the required properties and return the configuration
    try:
        config.read_file(open("/etc/fan-mode.conf"))
    except FileNotFoundError:
        print(
            'Configuration file not found. Please run "sudo fan-mode --setup" to create a new config file. Use "fan-mode --help" for more information.'
        )
        sys.exit(1)
    conf = get_config(["laptop", "fanint", "fan_name", "platform", "recover_mode"])
    return conf


def get_fan_status():  # Get the current fan status
    try:
        conf = run_checks()
        fan_name = conf[2]
        debug = subprocess.getoutput(f"sensors -u {fan_name}")
        output = debug.splitlines()
        for line in output:
            if "_input" in line:
                if "cpu" in output[output.index(line) - 1]:
                    print("CPU Fan Speed:", (float(line.split(":")[1].strip())), "RPM")
                elif "gpu" in output[output.index(line) - 1]:
                    print("GPU Fan Speed:", (float(line.split(":")[1].strip())), "RPM")
    except Exception as debug:
        print("N/A")
    return debug


def get_current_mode():  # Get the current fan mode
    conf = run_checks()
    platform = conf[3]
    fanint = conf[1]
    try:
        debug = subprocess.getoutput(
            f"cat /sys/devices/platform/{platform}/hwmon/hwmon{fanint}/pwm1_enable"
        )
        if debug == "2":
            print("Fan mode is set to auto.")
        elif debug == "0":
            print("Fan mode is set to full.")
    except Exception as debug:
        print("N/A")
    return debug


def get_temp():  # Get the current fan temperature
    try:
        debug = subprocess.getoutput("cat /sys/class/thermal/thermal_zone*/temp")
        cnt = 0
        linelist = []
        for line in debug.splitlines():
            linelist.append(line)
            cnt += 1
        print(f"CPU Temp:", (round((float(linelist[0]) / 1000))), f"{chr(176)}C")
        print(f"GPU Temp:", (round((float(linelist[1]) / 1000))), f"{chr(176)}C")
    except Exception as debug:
        print("N/A")
    return debug


def run_command(command, mode):  # Run a command and return the output
    debug = subprocess.getoutput(command)
    if debug == "2" or debug == "0":
        print(f"Fan mode set to {mode}.")
    elif "Permission denied" in debug:
        print("You need to run this script as root to use this option.")
        sys.exit(1)
    return debug


def set_fan_mode(mode):  # Set the fan mode
    conf = run_checks()
    platform = conf[3]
    fanint = conf[1]
    if mode == "auto":  # Set the fan mode to auto
        command = f'bash -c "tee /sys/devices/platform/{platform}/hwmon/hwmon{fanint}/pwm1_enable <<< 2"'
        debug = run_command(command, "auto")
    elif mode == "full":  # Set the fan mode to full speed
        command = f'bash -c "tee /sys/devices/platform/{platform}/hwmon/hwmon{fanint}/pwm1_enable <<< 0"'
        debug = run_command(command, "full")
    with open("/etc/fan-mode.conf", "w") as f:
        f.write(
            f"[fan-mode]\nlaptop = {conf[0]}\nfan_name = {conf[2]}\nfanint = {conf[1]}\nplatform = {conf[3]}\nrecover_mode = {mode}\n"
        )
    # TODO: Add support for GPU Fan control
    return debug


def recover_mode():  # Recover the fan mode after reboot
    conf = run_checks()
    recover_mode = conf[4]
    set_fan_mode(recover_mode)
    debug = f"Fan mode recovered to {recover_mode}."
    return debug


def main():  # Main function
    debug = None
    if "-d" in sys.argv or "--debug" in sys.argv:
        conf = run_checks()
        laptop = conf[0]
        print(
            f"Running {filename} version {version} by {author} in debug mode for {laptop}\n"
        )
    if "--help" in sys.argv or "-h" in sys.argv:  # Help
        print(
            f"""
Usage: {filename} [OPTION]

Set the fan mode of your Laptop.
    -a, --auto\t\t\tSet the fan mode to auto.
    -f, --full\t\t\tSet the fan mode to full speed.
    -s, --status\t\tGet the fan status.
    -r, --recover\t\tRecover last fan mode after reboot.
    -d, --debug\t\t\tPrint debug information.
    -v, --version\t\tPrint the version of this script.
    -h, --help\t\t\tShow this help message.
"""
        )
    elif "--auto" in sys.argv or "-a" in sys.argv:  # Set fan mode to auto
        debug = set_fan_mode("auto")
    elif "--full" in sys.argv or "-f" in sys.argv:  # Set the fan to full speed
        debug = set_fan_mode("full")
    elif "--recover" in sys.argv or "-r" in sys.argv:  # Recover the fan mode
        debug = recover_mode()
    elif "--status" in sys.argv or "-s" in sys.argv:  # Get the fan status
        debug = get_fan_status()
        debug1 = get_temp()
        debug2 = get_current_mode()
        debug += ("\n" + debug1) + ("\n" + debug2)
    elif "--version" in sys.argv or "-v" in sys.argv:  # Print the version
        print(f"{name} version {version} created by {author}.")
    elif "--setup" in sys.argv:  # Setup the configuration file
        chk = subprocess.getoutput("touch /etc/fan-mode.conf")
        if "Permission denied" in chk:
            print("You need to run this script as root to use this option.")
            sys.exit(1)
        else:
            lp_name = subprocess.getoutput("dmidecode -s system-product-name")
            with open("/etc/fan-mode.conf", "w") as f:
                f.write(
                    f'[fan-mode]\nlaptop = "{lp_name}"\nfan_name = "asus-isa-0000"\nfanint = *\nplatform = "asus-nb-wmi"\nrecover_mode = auto\n'
                )
            print("Configuration file created at /etc/fan-mode.conf")
    else:  # Invalid option
        print("Invalid argument. Use '-h' or '--help' for help.")
    if "-d" in sys.argv or "--debug" in sys.argv:  # Print debug information
        try:
            print("\n" + debug)
        except TypeError:
            pass
        except UnboundLocalError:
            pass


if __name__ == "__main__":  # Run the main function
    main()
