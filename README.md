html5spec.json
================================================================================

This repository contains Python code that generates machine-readable JSON
from the [WHATWG HTML Living Standard](https://html.spec.whatwg.org/multipage/)

This is an early work-in-progress and incomplete. Contributions are very
welcome.

See also: [HTML5 Relax NG schema](https://github.com/unsoup/validator/tree/gh-pages/schema-release/html5)


Scope & Mission Statement
--------------------------------------------------------------------------------

Much of HTML5 depends on context and subtle semantics. Checking this may either
be extremely computationally expensive, or express the intention of the author
in a way that not even a human reader can validate for certain. Additionally,
it is challenging to represent complex rules in a language-agnostic way.

This machine-readable specification will, therefore, always be incomplete.
Sometimes the best we can practically do is provide human-readable hints in
descriptions. Therefore, this machine-readable specification aims to assist a
human author and catch obvious errors - but not replace the human author.
