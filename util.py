import itertools
from collections import namedtuple
from typing import List


def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..., (sLast, None)"""
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.zip_longest(a, b, fillvalue=None)


def dict_lastitems(xs):
    """Iterates through a dict, generating a 3-tuple: `(key, value, last: bool)`
    where `last` is True iff it is the last item in the dict iterator.

    e.g. `xs -> (k0, v0, False), (k1, v1, False), ..., (kLast, vLast, True)`"""
    keys = pairwise(xs.keys())
    for key, key2 in keys:
        yield key, xs[key], key2 is None


def list_lastitems(xs):
    """Iterates through a list, generating a 2-tuple: `(item, last: bool)`
    where `last` is True iff it is the last item in the list iterator.

    e.g. `xs -> (x0, False), (x1, False), ..., (xLast, True)`"""
    for x, y in pairwise(xs):
        yield x, y is None


def dictify_namedtuples(xs: List[namedtuple]):
    """Convert a list of named tuples do a dict where the key is the first
    item in each tuple and each tuple has a unique key."""

    result = {}

    for x in xs:
        key = x[0]
        keyname = x._fields[0]
        r = {}

        for k, v in sorted(x._asdict().items()):
            if keyname == k:
                continue
            r[k] = v

        if key in result:
            # "Key %s already present - merge"
            t = result[key]
            for subkey in t.keys():
                if isinstance(t[subkey], str):
                    t[subkey] += ". " + r[subkey]
                elif isinstance(t[subkey], set):
                    t[subkey] = t[subkey].union(r[subkey])
                elif isinstance(t[subkey], list):
                    t[subkey].extend(r[subkey])
                else:
                    raise NotImplemented
        else:
            result[key] = r

    return result



