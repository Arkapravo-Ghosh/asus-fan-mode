#!/bin/bash
while true; do
    read -p "Do you wish to install this program? [y/N]: " yn
    case $yn in
        [Yy]* ) echo "Installing..." && pyinstaller --onefile --windowed src/main.py --name fan-mode && sudo cp dist/fan-mode /usr/bin/fan-mode && echo "Installed."; break;;
        [Nn]* ) echo "Aborted."; exit;;
        * ) echo "Aborted."; exit;;
    esac
done