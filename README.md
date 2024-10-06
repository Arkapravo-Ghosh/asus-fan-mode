
# ASUS Fan Mode Controller
Fan Mode Control for Asus Vivobook 14X Pro OLED on Linux

## Automatic Fan Control Based on Temperature

The `fan-mode-recovery` service automatically adjusts the fan speed based on the system's CPU temperature.

- **When the CPU temperature exceeds 87°C**: The fan is automatically set to 100% speed to cool down the system.
- **When the CPU temperature exceeds 82°C**: The fan is automatically set to 80% speed to keep the temperature under control.
- **When the CPU temperature exceeds 77°C**: The fan is automatically set to 60% speed.
- **When the CPU temperature drops below 77°C**: The fan mode is switched back to auto, allowing the system to regulate the fan speed based on normal usage.

This automatic control ensures that the system remains cool during high load and returns to quieter, more energy-efficient operation when the temperature is back to normal levels.

You can still manually set the fan mode to full or auto using the following commands if needed:

- **Full fan speed**:

    ```bash
    sudo fan-mode --full
    ```

- **Auto mode**:

    ```bash
    sudo fan-mode --auto
    ```



![](https://img.shields.io/github/license/Arkapravo-Ghosh/asus-fan-mode)
![](https://img.shields.io/badge/platform-Linux-blue)

This project allows you to control the fan speed of the Asus Vivobook 14X Pro OLED on Linux based on the temperature of the system. It uses the `k10temp` sensor for monitoring the CPU temperature and adjusts the fan speed accordingly.

## Installation

### Prerequisites

Before installing the fan mode controller, ensure that the following dependencies are installed:

1. **lm-sensors** and **fancontrol**: Required for monitoring system temperatures and controlling the fan.
2. **xsensors**: Optional GUI tool for visualizing sensor data.

You can install these packages on Debian-based systems like Ubuntu or Linux Mint with the following command:

```bash
sudo apt-get install lm-sensors fancontrol xsensors
```

Once installed, run the following command to detect your system's sensors:

```bash
sudo sensors-detect
```

Answer "Yes" to all the prompts to ensure proper sensor detection.

### Cloning the Repository

To install `asus-fan-mode`, clone this repository and navigate to the project directory:

```bash
git clone https://github.com/Gerald-Ha/asus-fan-mode.git
cd asus-fan-mode
```

### Installation Guide

You can use the provided `install.sh` script to install the fan mode controller and set it up as a background service. The script will also handle setting up the necessary files.

```bash
sudo ./install.sh
```

This will:
- Copy the Python script to `/opt/fan-mode/` and create a symlink in `/usr/bin/fan-mode`.
- Set up a `systemd` service that runs the fan control automatically in the background based on system temperature.

### Systemd Service

The installation script will create a `systemd` service that automatically adjusts the fan mode on startup. You can manage the service using the following commands:

- **Enable the service** (if not already enabled):

    ```bash
    sudo systemctl enable fan-mode-recovery
    ```

- **Start the service**:

    ```bash
    sudo systemctl start fan-mode-recovery
    ```

- **Stop the service** (to manually control the fan):

    ```bash
    sudo systemctl stop fan-mode-recovery
    ```

- **Disable the service** (to prevent it from starting at boot):

    ```bash
    sudo systemctl disable fan-mode-recovery
    ```

## Usage

Once installed, you can use the following commands to manually control or check the status of the fan:

- **Set fan mode to auto** (adjusts fan speed automatically based on temperature):

    ```bash
    sudo fan-mode --auto
    ```

- **Set fan mode to full** (forces the fan to run at full speed):

    ```bash
    sudo fan-mode --full
    ```

- **Check the current fan status**:

    ```bash
    sudo fan-mode --status
    ```

- **Generate a default configuration file**:

    ```bash
    sudo fan-mode --setup
    ```

For more options, use the help command:

```bash
fan-mode --help
```

## Disabling Automatic Recovery of Fan Mode on Reboot

To disable the automatic recovery of the fan mode on reboot, disable the systemd service:

```bash
sudo systemctl disable fan-mode-recovery
```

## Miscellaneous

- **`clean.sh`**: This script cleans all build files created during the installation or compilation of the project. Note: It does not uninstall the program.

    ```bash
    sudo ./clean.sh
    ```

- **`compile.sh`**: This script compiles the project. Note: It does not install the program.

    ```bash
    sudo ./compile.sh
    ```

Before running the compile script, ensure all dependencies are installed by running:

```bash
sudo pip3 install -r requirements.txt
```

## Known Issues

- GPU Fan Controlling is not supported yet.

## Contribution

Feel free to contribute to this project by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
