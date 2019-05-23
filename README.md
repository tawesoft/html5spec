html5spec
================================================================================

This repository contains Python code that generates machine-readable JSON
from the [WHATWG HTML Living Standard](https://html.spec.whatwg.org/multipage/)
and [Accessible Rich Internet Applications (WAI-ARIA)](https://w3c.github.io/aria/)

This is a work-in-progress and incomplete without a stable format.
Contributions are very welcome. Regardless, even in this undeveloped state,
this project is still a good basis for many real-world applications.

See also: [HTML5 Relax NG schema](https://github.com/unsoup/validator/tree/gh-pages/schema-release/html5)

Type `make` to download and parse the spec.


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


Projects using html5spec.json
--------------------------------------------------------------------------------

* [strictdom](https://github.com/tawesoft/strictdom)

Please open an issue or pull request to add a project to this list.

