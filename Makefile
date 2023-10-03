.PHONY: run clean

venv/bin/activate: requirements.txt
	python3 -m venv venv
	# ./venv/bin/pip freeze > requirements.txt
	./venv/bin/pip install -r requirements.txt

run: venv/bin/activate
	./venv/bin/python3 ./slide01/capital_budget.py

clean:
	rm -rf __pycache__
	rm -rf venv