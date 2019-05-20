.PHONY: default clean
default: all ;

specs=indices.html dom.html input.html

clean:
	rm -f $(specs)
	rm -f aria.html

aria.html:
	wget -O aria.html https://w3c.github.io/aria/

%.html:
	wget -O $@ https://html.spec.whatwg.org/multipage/$@

all: $(specs) aria.html
