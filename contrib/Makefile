.PHONY: default clean
default: all ;

specs=indices.html dom.html input.html syntax.html

clean:
	rm -f timestamp
	rm -f $(specs)
	rm -f aria.html

aria.html:
	wget -O aria.html https://w3c.github.io/aria/

%.html:
	wget -O $@ https://html.spec.whatwg.org/multipage/$@

timestamp:
	date -u > timestamp

all: timestamp $(specs) aria.html
