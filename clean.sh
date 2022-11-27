#!/bin/bash
while true; do
    read -p "Do you wish to clean all the build files? [y/N]: " yn
    case $yn in
        [Yy]* ) echo "Cleaning..." && rm -rf dist build fan-mode.spec && echo "Done."; break;;
        [Nn]* ) echo "Aborted."; exit;;
        * ) echo "Aborted."; exit;;
    esac
done