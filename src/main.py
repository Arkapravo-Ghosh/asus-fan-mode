#!/bin/python3
import sys
import subprocess
import configparser
import time

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

def get_k10temp_temperature():  # Get the k10temp temperature
    try:
        debug = subprocess.getoutput("sensors | grep 'Tctl'")
        temp_value = float(debug.split(":")[1].strip().split('°')[0])
        print(f"k10temp Tctl temperature: {temp_value} °C")
        return temp_value
    except Exception as debug:
        print("N/A")
        return None

def control_fan_based_on_temperature():  # Control the fan speed based on temperature
    current_temp = get_k10temp_temperature()

    if current_temp is not None:
        if current_temp >= 80:  # Angepasster Schwellenwert
            print("Setting fans to maximum speed (full mode)")
            set_fan_mode("full")
        elif current_temp < 67:
            print("Setting fans to auto mode")
            set_fan_mode("auto")

def run_command(command, mode):  # Run a command and return the output
    debug = subprocess.getoutput(command)
    if debug == "2" or debug == "0":
        print(f"Fan mode set to {mode}.")
    elif "Permission denied" in debug:
        print("You need to run this script as root to use this option.")
        sys.exit(1)
    return debug

def set_fan_mode(mode):  # Set the fan mode
    platform = "asus-nb-wmi"  # Feste Zuweisung
    fanint = "5"  # Festes hwmon5, basierend auf deinem System
    if mode == "auto":  # Set the fan mode to auto
        command = f'bash -c "tee /sys/devices/platform/{platform}/hwmon/hwmon{fanint}/pwm1_enable <<< 2"'
        debug = run_command(command, "auto")
    elif mode == "full":  # Set the fan mode to full speed
        command = f'bash -c "tee /sys/devices/platform/{platform}/hwmon/hwmon{fanint}/pwm1_enable <<< 0"'
        debug = run_command(command, "full")
    return debug

def monitor_temperature(interval=10):  # Überwacht die Temperatur alle 10 Sekunden
    while True:
        control_fan_based_on_temperature()
        time.sleep(interval)  # Pause für das angegebene Intervall (in Sekunden)

def main():  # Main function
    if "-d" in sys.argv or "--debug" in sys.argv:
        print(
            f"Running {filename} version {version} by {author} in debug mode\n"
        )
    if "--auto" in sys.argv or "-a" in sys.argv:  # Set fan mode to auto
        set_fan_mode("auto")
    elif "--full" in sys.argv or "-f" in sys.argv:  # Set the fan to full speed
        set_fan_mode("full")
    elif "--status" in sys.argv or "-s" in sys.argv:  # Get the fan status and monitor
        monitor_temperature(interval=10)  # Überprüft die Temperatur alle 10 Sekunden
    else:
        print("Invalid argument. Use '-h' or '--help' for help.")

if __name__ == "__main__":  # Run the main function
    main()
