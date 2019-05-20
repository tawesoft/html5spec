.PHONY: default clean
default: all ;

clean:
	make -C contrib clean
	rm -f bin/*.json

_contrib:
	make -C contrib

json:
	python3 parse.py
	# generates `spec-json/*.json`, etc.
	# run `make -B json` to force this to update

all: _contrib json

