.PHONY: run

run: main.dat

main.dat: main.py
	python3 main.py main.dat

clean: 
	rm -f *.dat

.PHONY: main.dat clean

