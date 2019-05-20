.PHONY: default clean
default: all ;

clean:
	make -C contrib clean
	rm -f bin/*.json

_contrib:
	make -C contrib

json: _contrib
	python3 parse.py
	# generates `spec-json/*.json`, etc.

all: _contrib json

