# Installation

## Prerequisites

Install the following packages:

- [lm_sensors](https://github.com/lm-sensors/lm-sensors)
- [make](https://www.gnu.org/software/make)

### Arch Linux

```shell
sudo pacman -Syy lm_sensors make
```

### Debian/Ubuntu Linux

```shell
sudo apt update
sudo apt install lm-sensors make
```

### Fedora Linux

```shell
sudo dnf install lm_sensors make
```

### Red Hat Enterprise Linux

```shell
sudo yum install lm_sensors make
```

### OpenSUSE Linux

```shell
sudo zypper install sensors make
```

### Gentoo Linux

#### Install as a dependency

1. Add these USE flags in `/etc/portage/make.conf`:

   ```
   contrib
   sensord
   static-libs
   ```

2. Emerge:

   ```shell
   sudo emerge --ask --changed-use --deep @world
   ```

#### OR Install directly

```shell
sudo emerge --ask sys-apps/lm-sensors
```

### Alpine Linux

```shell
sudo apk add lm_sensors lm_sensors-detect perl make
```

```shell
sudo tee /etc/modules-load.d/i2c.conf <<< i2c-dev
```

```shell
sudo modprobe i2c-dev
```

```shell
sudo rc-update add lm_sensors default
```

```shell
sudo rc-update add sensord default
```

```shell
sudo /etc/init.d/lm_sensors start && sudo /etc/init.d/sensord start
```

```shell
sudo lbu commit
```

## Install asus-fan-mode

Run the following commands in the terminal:

```shell
git clone https://github.com/Arkapravo-Ghosh/asus-fan-mode.git
```

```shell
cd asus-fan-mode
```

```shell
make install
```
