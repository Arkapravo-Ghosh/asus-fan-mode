#!/bin/bash
while true; do
    read -p "Do you wish to install this program? [y/N]: " yn
    case $yn in
        [Yy]* ) 
            echo "Installing..."

            
            sudo rm -rf /opt/fan-mode /usr/bin/fan-mode

            
            sudo mkdir -p /opt/fan-mode
            sudo cp -r src/main.py /opt/fan-mode/fan-mode.py

            
            sudo ln -s /opt/fan-mode/fan-mode.py /usr/bin/fan-mode

            
            sudo cp fan-mode-recovery.service /etc/systemd/system/
            sudo systemctl daemon-reload
            sudo systemctl enable fan-mode-recovery
            sudo systemctl start fan-mode-recovery

            echo "Installed."
            break;;
        [Nn]* ) 
            echo "Aborted."
            exit;;
        * ) 
            echo "Aborted."
            exit;;
    esac
done
