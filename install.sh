#!/bin/bash
echo "Installing..."
pyinstaller --onefile --windowed src/main.py --name fan-mode
sudo cp dist/fan-mode /usr/bin/fan-mode
echo "Done."