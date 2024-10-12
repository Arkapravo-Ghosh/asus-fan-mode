TARGET_NAME := fan-mode
PYINSTALLER_FLAGS := --noconfirm --onedir --windowed src/main.py --name $(TARGET_NAME)
DIST_DIR := dist/$(TARGET_NAME)
BUILD_DIR := build
SPEC_FILE := $(TARGET_NAME).spec
SYSTEMD_SERVICE := $(TARGET_NAME)-recovery.service
REQUIRED_SYSTEM_TOOLS := python3 objdump

.DEFAULT_GOAL := help

help:
	@echo "Usage: make [target]\n"
	@echo "  clean  	Clean all the build files."
	@echo "  compile	Compile the program."
	@echo "  install	Install the program."
	@echo "  remove 	Uninstall the program."
	@echo "  check  	Check for required tools."

check:
	@missing_tools=; \
	for tool in $(REQUIRED_SYSTEM_TOOLS); do \
		if ! command -v $$tool >/dev/null 2>&1; then \
			missing_tools="$$missing_tools $$tool"; \
		fi; \
	done; \
	if [ -n "$$missing_tools" ]; then \
		echo "Error: The following tools are missing:$$missing_tools"; \
		exit 1; \
	else \
		echo "All required system tools are available."; \
	fi

clean:
	@echo "Cleaning..."
	@rm -rf dist $(BUILD_DIR) $(SPEC_FILE)
	@echo "Clean complete."

compile: check
	@echo "Compiling..."
	@python3 -m venv .venv && \
	. .venv/bin/activate && \
	pip3 install pyinstaller && \
	pyinstaller $(PYINSTALLER_FLAGS) && \
	echo "Compiled. Check '$(DIST_DIR)' for the binary and '$(BUILD_DIR)' for the build files."

install: compile
	@echo "Installing..."
	sudo rm -rf /opt/$(TARGET_NAME) /usr/bin/$(TARGET_NAME)
	sudo cp -r $(DIST_DIR) /opt/$(TARGET_NAME)
	sudo ln -s /opt/$(TARGET_NAME)/$(TARGET_NAME) /usr/bin/$(TARGET_NAME)
	sudo cp $(SYSTEMD_SERVICE) /etc/systemd/system/
	sudo $(TARGET_NAME) --setup
	sudo systemctl daemon-reload
	sudo systemctl enable --now $(SYSTEMD_SERVICE)
	@echo "Installation complete."

remove:
	@echo "Removing..."
	sudo systemctl disable --now $(SYSTEMD_SERVICE)
	sudo rm -rf /opt/$(TARGET_NAME) /usr/bin/$(TARGET_NAME) /etc/fan-mode.conf /etc/systemd/system/$(SYSTEMD_SERVICE)
	@echo "Removal complete."
