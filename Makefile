.PHONY: default
default: all ;

src:
    make -C src

parse: src
    python3 parse.py
    # generates bin/*.json

all: parse

