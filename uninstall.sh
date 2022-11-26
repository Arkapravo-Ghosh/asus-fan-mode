#!/bin/bash
while true; do
    read -p "Do you wish to uninstall this program? [y/N]: " yn
    case $yn in
        [Yy]* ) sudo rm -f /usr/bin/fan-mode && echo "Uninstalled."; break;;
        [Nn]* ) echo "Aborted."; exit;;
        * ) echo "Aborted."; exit;;
    esac
done