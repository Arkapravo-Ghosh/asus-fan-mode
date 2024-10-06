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

def get_config(conf_list):  
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

def run_checks():  
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

def control_fan_based_on_temperature():  
    current_temp = get_k10temp_temperature()

    if current_temp is not None:
        if current_temp >= 87:  # Set fans to 100% when temp reaches 87°C
            print("Setting fans to 100% speed (full mode)")
            set_fan_mode("full")
        elif current_temp >= 82:  # Set fans to 80% when temp reaches 82°C
            print("Setting fans to 80% speed")
            set_fan_speed(80)
        elif current_temp >= 77:  # Set fans to 60% when temp reaches 77°C
            print("Setting fans to 60% speed")
            set_fan_speed(60)
        else:
            print("Setting fans to auto mode")
            set_fan_mode("auto")

def set_fan_speed(percentage):  
    platform = "asus-nb-wmi"  
    fanint = "5"  
    pwm_value = int(percentage * 255 / 100)  
    command = f'bash -c "tee /sys/devices/platform/{platform}/hwmon/hwmon{fanint}/pwm1 <<< {pwm_value}"'
    run_command(command, f"{percentage}% speed")

def run_command(command, mode):  
    debug = subprocess.getoutput(command)
    if debug == "2" or debug == "0":
        print(f"Fan mode set to {mode}.")
    elif "Permission denied" in debug:
        print("You need to run this script as root to use this option.")
        sys.exit(1)
    return debug

def set_fan_mode(mode): 
    platform = "asus-nb-wmi"  
    fanint = "5"  
    if mode == "auto":  
        command = f'bash -c "tee /sys/devices/platform/{platform}/hwmon/hwmon{fanint}/pwm1_enable <<< 2"'
        debug = run_command(command, "auto")
    elif mode == "full":  
        command = f'bash -c "tee /sys/devices/platform/{platform}/hwmon/hwmon{fanint}/pwm1_enable <<< 0"'
        debug = run_command(command, "full")
    return debug

def monitor_temperature(interval=3):  # Temperatur Scan alle 3 Sekunden
    while True:
        control_fan_based_on_temperature()
        time.sleep(interval)  

def main():  
    if "-d" in sys.argv or "--debug" in sys.argv:
        print(
            f"Running {filename} version {version} by {author} in debug mode\n"
        )
    if "--auto" in sys.argv or "-a" in sys.argv:  
        set_fan_mode("auto")
    elif "--full" in sys.argv or "-f" in sys.argv:  
        set_fan_mode("full")
    elif "--status" in sys.argv or "-s" in sys.argv:  
        monitor_temperature(interval=4)  
    else:
        print("Invalid argument. Use '-h' or '--help' for help.")

if __name__ == "__main__":  
    main()
