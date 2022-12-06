# Installation
<details>
  <summary>
    Prerequisites: Install <a href="https://github.com/lm-sensors/lm-sensors">lm_sensors</a> package (Click to expand)
  </summary>
  
  ### Arch Linux
  `sudo pacman -Syy lm_sensors`
  ### Debian/Ubuntu Linux
  `sudo apt update`\
  `sudo apt install lm-sensors`
  ### Fedora Linux
  `sudo dnf install lm_sensors`
  ### Red Hat Enterprise Linux
  `sudo yum install lm_sensors`
  ### OpenSUSE Linux
  `sudo zypper install sensors`
  ### Gentoo Linux
  <details>
    <summary>
      Install as a dependency
    </summary>
    
  ##### Add these USE Flags in `/etc/portage/make.conf`:
  `contrib`\
  `sensord`\
  `static-libs`
  ##### Emerge
  `sudo emerge --ask --changed-use --deep @world`
  </details>
  
  OR
  
  <details>
    <summary>
      Install directly
    </summary>
    
  `sudo emerge --ask sys-apps/lm-sensors`
  </details>
  
  ### Alpine Linux
  `sudo apk_add lm_sensors lm_sensors-detect perl`\
  `sudo tee /etc/modules-load.d/i2c.conf <<< i2c-dev`\
  `sudo modprobe i2c-dev`\
  `sudo rc-update add lm_sensors default`\
  `sudo rc-update add sensord default`\
  `sudo /etc/init.d/lm_sensors start && sudo /etc/init.d/sensord start`\
  `sudo lbu commit`

</details>


## Install asus-fan-mode
> Run the following in terminal:
```
git clone https://github.com/Arkapravo-Ghosh/asus-fan-mode.git
cd asus-fan-mode
sudo pip3 install -r requirements.txt
./install.sh
```
> Run the command `fan-mode` to launch the program.
> To uninstall, run [`./uninstall.sh`](uninstall.sh) in terminal.

