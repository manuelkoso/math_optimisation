DIR = slide01
SRC = main.py

.PHONY: run clean setup

setup: requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt

run: setup
	./venv/bin/python3 ./$(DIR)/$(SRC)

clean:
	rm -rf __pycache__
	rm -rf venv