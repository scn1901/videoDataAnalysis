.PHONY: run

run: main.pyc

main.pyc: main.py Data.py
	python3 main.py main.pyc

Data.pyc: Data.py
	python3 Data.py Data.pyc


clean: 
	rm -f *.pyc

.PHONY: main.pyc clean

