#!/bin/bash
while true; do
    read -p "Do you wish to install this program? [y/N]: " yn
    case $yn in
        [Yy]* ) echo "Compiling..."; rm -rf build dist fan-mode.spec; pyinstaller --noconfirm --onedir --windowed src/main.py --name fan-mode; echo "Compiled. Check 'dist/fan-mode' directory for the compiled binary and 'build' directory for the build files."; break;;
        [Nn]* ) echo "Aborted."; exit;;
        * ) echo "Aborted."; exit;;
    esac
done