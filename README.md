html5spec
================================================================================

This repository contains Python code that generates machine-readable JSON
from the [WHATWG HTML Living Standard](https://html.spec.whatwg.org/multipage/)
and [Accessible Rich Internet Applications (WAI-ARIA)](https://w3c.github.io/aria/)

This is a work-in-progress and incomplete without a stable format.
Contributions are very welcome. Regardless, even in this undeveloped state,
this project is still a good basis for many real-world applications.

Type `make` to download and parse the spec.

This repo currently contains a spec as of 2020, and only
[small updates](https://github.com/tawesoft/html5spec/issues/6)
are needed to support the spec as of December 2024.


Alternatives / see also
------------------------

* [strictdom](https://github.com/tawesoft/strictdom) - uses this repo to create a strict wrapper over [dominate](https://github.com/Knio/dominate), a Python library for creating and manipulating HTML documents .
* [HTML5 Relax NG schema](https://github.com/unsoup/validator/tree/gh-pages/schema-release/html5)
* [Gostar - a fluent HTML builder for Go built directly from the HTML Living Standard](https://github.com/delaneyj/gostar)
    + similarly, this [contains a spec encoded as Go](https://github.com/delaneyj/gostar/blob/main/cfg/spec_html.go)


Scope & Mission Statement
--------------------------------------------------------------------------------

Much of HTML5 depends on context and subtle semantics. Checking this may either
be extremely computationally expensive, or express the intention of the author
in a way that not even a human reader can validate for certain. Additionally,
it is challenging to represent complex rules in a language-agnostic way.

This machine-readable specification will, therefore, always be incomplete.
Sometimes the best we can practically do is provide human-readable hints in
descriptions. Therefore, this machine-readable specification aims to assist a
human author and catch obvious errors - but not replace the human author
entirely.



