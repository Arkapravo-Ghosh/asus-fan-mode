#!/bin/bash
while true; do
    read -p "Do you wish to install this program? [y/N]: " yn
    case $yn in
        [Yy]* ) echo "Installing..."; rm -rf build dist fan-mode.spec; pyinstaller --noconfirm --onedir --windowed src/main.py --name fan-mode; sudo rm -rf /opt/fan-mode /usr/bin/fan-mode; sudo cp -r dist/fan-mode /opt/fan-mode; sudo ln -s /opt/fan-mode/fan-mode /usr/bin/fan-mode; sudo cp fan-mode-recovery.service /etc/systemd/system/; sudo systemctl daemon-reload; sudo systemctl enable fan-mode-recovery; echo "Installed."; break;;
        [Nn]* ) echo "Aborted."; exit;;
        * ) echo "Aborted."; exit;;
    esac
done
