from util import *
import types


def pformat_list(xs, indent=0):
    t = "    "*indent

    if not xs:
        yield "[]"
        return

    yield t + "[\n"
    for value, last in list_lastitems(sorted(xs)):
        yield from pformat(value, indent+1)
        if not last: yield ","
        yield "\n"
    yield t + "]"


def pformat_set(xs, indent=0):
    t = "    "*indent

    if not xs:
        yield "{}"
        return

    if xs and len(xs) == 1:
        yield "{"
        yield repr(next(iter(xs)))
        yield "}"
        return

    yield t + "{\n"
    for value, last in list_lastitems(sorted(xs)):
        if isinstance(value, str):
            yield from pformat(value, indent+1)
        if not last: yield ","
        yield "\n"
    yield t + "}"


def pformat_dict(xs, indent=0):
    t = "    "*indent

    if not xs:
        yield "{}"
        return

    yield t + "{\n"
    for key, last in list_lastitems(sorted(xs.keys())):
        value = xs[key]
        yield t + "    %s:" % repr(key)
        if isinstance(value, str):
            yield " "
            yield repr(value)
        else:
            if isinstance(value, types.GeneratorType):
                value = list(value)
            yield "\n" if (value and ("\n" in pformat(value))) else " "
            yield from pformat(value, indent+1)
        if not last: yield ","
        yield "\n"
    yield t + "}"


def pformat(xs, indent=0):
    if isinstance(xs, types.GeneratorType):
        yield from pformat_list(list(xs), indent)
    elif isinstance(xs, tuple):
        yield "    "*indent + "<tuple>"+repr(xs)
    elif isinstance(xs, str):
        yield "    "*indent + repr(xs)
    elif isinstance(xs, set):
        yield from pformat_set(xs, indent)
    elif isinstance(xs, dict):
        yield from pformat_dict(xs, indent)
    elif isinstance(xs, list):
        yield from pformat_list(xs, indent)
    else:
        yield "    "*indent + str(type(xs)) + ":" + repr(xs)