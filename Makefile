SHELL = bash
.DEFAULT_GOAL := help

VENV = venv
BIN=$(VENV)/bin

# make it work on windows too
ifeq ($(OS), Windows_NT)
    BIN=$(VENV)/Scripts
    PY=python
endif

help: ## show list of all command and there help text
	@cat $(MAKEFILE_LIST) | egrep '^[a-zA-Z0-9_]+:.*' | \
	awk 'BEGIN { FS = ":.*?##"}; { printf "%-20s :%s\n", $$1, $$2 }'


build: ## create vertualenv and install all dependencies
	@python3 -m venv venv
	@$(BIN)/pip3 install -r requirements_dev.txt
	@$(BIN)/pip3 install -r requirements.txt
	@$(BIN)/pip3 install -e .

rotor: ## build rotors and save them to data/rotors.enigma
	@$(BIN)/python3 src/enigma/rotor.py

run: ## run the application
	@$(BIN)/python3 src/enigma/main.py
