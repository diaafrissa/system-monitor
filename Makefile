PYTHON = python3
PIP = pip3

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) monitor_web.py

test:
	$(PYTHON) test_web.py

clean:
	rm -rf __pycache__
	rm -rf templates/__pycache__
