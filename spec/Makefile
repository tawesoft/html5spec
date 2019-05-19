.PHONY: default clean
default: all ;

specs=indices.html dom.html input.html

clean:
	rm $(specs)

%.html:
	wget -O $@ https://html.spec.whatwg.org/multipage/$@

all: $(specs)

