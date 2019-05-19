.PHONY: default clean
default: all ;

clean:
	make -C spec clean
	rm bin/*.json

_spec:
	make -C spec

parse: _spec
	python3 parse.py
	# generates bin/*.json

all: _spec parse

